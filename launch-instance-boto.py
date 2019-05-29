import os
import time
import boto
import boto.manage.cmdshell

def launch_instance(ami='ami-7341831a',
                    instance_type='t1.micro',
                    key_name='paws',
                    key_extension='.pem',
                    key_dir='~/.ssh',
                    group_name='paws',
                    ssh_port=22,
                    cidr='0.0.0.0/0',
                    tag='paws',
                    user_data=None,
                    cmd_shell=True,
                    login_user='ec2-user',
                    ssh_password=None):
    """
    launch instance and wait for it to running
    """
    cmd = None
    #connection to ec2 service
    ec2 = boto.connect_ec2()
    #check keypair
    try:
        key = ec2.get_all_key_pairs(keynames=[key_name])[0]
    except ec2.ResponseError, e:
        if e.code == 'InvalidKeyPair.NotFound':
            print 'creating keypair: %s' % key_name
            #create ssh key to logging into instances
            key = ec2.create_key_pair(key_name)

            #aws will store public
            key.save(key_dir)
        else:
            raise

    # check security if exist
    try:
        group = ec2.get_all_security_groups(groupnames=[group_name])[0]
    except ec2.ResponseError, e:
        if e.code == 'InvalidGroup.NotFound':
            print 'creating security group: %s' % group_name
            #create a security group control access for ssh
            group = ec2.create_security_group(group_name,
                            'a group allows for ssh')
        else:
            raise
    #add rule to security group for ssh traffic
    try:
        group.authorize('tcp', ssh_port, ssh_port, cidr)
    except ec2.ResponseError, e:
        if e.code == 'InvalidPermission.Duplicate':
            print 'security group: %s already authorized' % group_name
        else:
            raise

    #start the instance process
    reservation = ec2.run_instances(ami,
                                    key_name=key_name,
                                    security_groups=[group_name],
                                    instance_type=instance_type,
                                    user_data=user_data)

    instance = reservation.instances[0]
    print "waiting for instance"
    while instance.state != "running":
        print '.'
        time.sleep(5)
        instance.update()
