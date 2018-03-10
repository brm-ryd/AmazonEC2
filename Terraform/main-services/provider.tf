terraform {
  backend "s3" {
    bucket = "mainservices-terraform-state"
    key    = "test-main.tfstate"
    region = "ap-southeast-1"
  }
}
