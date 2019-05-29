/*
data "tf_remote_state" "db" {
  backend = "s3"

  config {
    bucket = "(buck_test)"
    key = "/stage/data-stores/mysql/terraform.tfstate"
    region = "ap-southeast-1"
  }
}
*/
module "webserver_cluster" {
  source = "../../../../services/webserver-cluster/vars.tf"
  cluster_name = "webserver-stg"
  db_remote_state_bucket = "(buck_test)"
  #db_remote_state_key = "stage/data-storage/mysql/*.tfstate" -- not stored inside directory
  instance_type = "t2.micro"
  min_size = 2
  max_size = 2
  enable_autoscaling = false
}
