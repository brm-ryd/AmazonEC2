resource "aws_security_group" "instance" {
    name = "security apply"

    ingress {
      from_port = 8080
      to_port = 8080
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
}
