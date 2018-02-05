resource "aws-instance" "app" {
  instance_type = "t2.micro"
  availability_zone = "ap-southeast-1"
  ami = "ami-20d45612"

  user_data = << EOF
          #!/bin/bash
          sudo service nginx start
          EOF
}
