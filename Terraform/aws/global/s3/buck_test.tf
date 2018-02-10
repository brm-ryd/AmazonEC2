resource "aws_s3_bucket" "terraform_state" {
    bucket = "buck_test"
    region = "ap-southeast-1"

    versioning {
      enabled = true
    }

    lifecycle_rule {
      prevent_destroy = true
    }
}
