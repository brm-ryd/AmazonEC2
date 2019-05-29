provider "aws" {
  region = "ap-southeast-1"
}

resource "aws-dbmysql-instance" "DB-Master1" {
  engine = "mysql"
  allocated_storage = 10
  instance_class = "db.t2.micro"
  name = "DB Master 1"
  username = "${var.db_username}"
  password = "${var.db_password}"
}
