data "aws_secretsmanager_secret" "postgresql_password_secret" {
  name = "RDSPostgresPassword"
}

data "aws_secretsmanager_secret_version" "rds_password" {
  secret_id = "RDSPostgresPassword"
}