# username, password, etc ...
# need use encryption using hashicorp vault/password manager(lastpass,1password)
# expose secrets to Terraform via environment variables
# > export TF_VAR_db_password = "(DB_PASSWORD)"

variable "db_username" {
  description = "username database"
  #...
}

variable "db_password" {
  description = "password database"
  #...
}
