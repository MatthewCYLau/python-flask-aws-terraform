data "aws_secretsmanager_secret" "postgresql_password_secret" {
  name = local.rds_postgress_password_secret_name
}

data "aws_secretsmanager_secret_version" "rds_password" {
  secret_id = local.rds_postgress_password_secret_name
}