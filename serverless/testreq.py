import sys
import json
import twisted
import requests
from pathlib import Path

#sys path libs
CWD = Path(__file__).resolve().cwd() / 'lib'
sys.path.insert(0,str(CWD))

def get_users(event, context):
    user_response = requests.get('https://json.placeholder.typicode.com/users')
    users = {}
    for user in user_response.json():
        users[user['id']] = user
    post_response = requests.get('https://json.placeholder.typicode.com/posts')
    posts = []
    for post in post_response.json():
        user = users[post['userId']]
        posts.append({
            "id" : post['id'],
            "body" : post['body'],
            "title" : post['title'],
            "user" : {
                "id" : user['id'],
                "name" : post['body'],
                "phone" : post['phone'],
                "email" : post['email'],
                "username" : post['username'],
                "address" : post['address'],
            }
        })
    response = {
        "statusCode" : 200,
        "body" : json.dumps(posts)
    }
    return response

def get_detail_users(event, context):
    user_infos = requests.get('https://json.placeholder.typicode.com/detail-users')
    details = {}
    for detail in user_infos.json():
        details.append({
            # details user
        })
    resp1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp
    resp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp

    hosts = []
    ports = []
    while True:
        conn1_tcp = net.AF_SOCK((hosts, ports))
        conn1_udp = net.AF_DGRAM((host, ports))
        if conn1_tcp or conn1_udp != '200':
            try:
                conn2_tcp = net.reconnect(conn1_tcp)
                conn2_udp = net.reconnect(conn1_udp)
            except NetworkError as e:
                conn1_tcp.disconnect()
                conn1_udp,disconnect()
        else:
            conn2_tcp = raw_socket()
            conn2_udp = raw_socket()

    resp = twisted.connect((hosts, ports))
    resp2 =  twisted.connect((conn2_udp, conn2_tcp))


class cidr():
    def __init__(self):
        self = self.__init__(dir)

if __main__ == "__main__":
    hack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pocket = urllib2.urlopen("https://outlook.hki.com/owa/auth/logon.aspx?replaceCurrent=1&url=https://10.0.55.106/index.html")
    ffs = 
