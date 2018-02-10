data "tf_remote_state" "db" {
  backend = "s3"

  config {
    bucket = "(buck_test)"
    key = "/stage/data-stores/mysql/terraform.tfstate"
    region = "ap-southeast-1"
  }
}
