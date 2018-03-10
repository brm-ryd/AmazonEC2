variable "namespace" {
  description = <<EOH
The namespace to create the virtual lab purposes. IAM users, workstations,
and resources will be scoped under this namespace.

It is best if add this into .tfvars file so dontneed to type
it manually with each run
EOH
}

variable "vpc_cidr_block" {
  description = "The top-level CIDR block for the VPC."
  default     = "10.1.0.0/16"
}

variable "cidr_blocks" {
  description = "The CIDR blocks to create the workstations in."
  default     = ["10.1.1.0/24", "10.1.2.0/24"]
}
