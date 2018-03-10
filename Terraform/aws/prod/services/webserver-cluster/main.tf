module "webserver_cluster" {
  source = "../../../../services/webserver-cluster/vars.tf"
  cluster_name = "webservers-prod"
  db_remote_state_bucket = "(buck_test)"
  #db_remote_state_key = "stage/data-storage/mysql/.tfstate" -- not stored inside directory
  instance_type = "m4.large"
  min_size = 2
  max_size = 10
  enable_autoscaling = true
}
