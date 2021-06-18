resource "aws_db_instance" "postgres" {
  allocated_storage      = 10
  engine                 = "postgres"
  engine_version         = "9.6.20"
  instance_class         = "db.t3.micro"
  name                   = "flaskdb"
  username               = "foo"
  password               = jsondecode(data.aws_secretsmanager_secret_version.rds_password.secret_string)["POSTGRES_PASSWORD"]
  skip_final_snapshot    = true
  db_subnet_group_name   = aws_db_subnet_group.postgres.name
  vpc_security_group_ids = [aws_security_group.rds.id]
}

resource "aws_db_subnet_group" "postgres" {
  name       = "postgres-subnet"
  subnet_ids = [aws_subnet.pub_subnet.id, aws_subnet.pub_subnet2.id]

  tags = {
    Name = "PostgreSQL DB subnet group"
  }
}

resource "aws_security_group" "rds" {
  name        = "rds-sg"
  vpc_id      = aws_vpc.vpc.id
  description = "allow inbound access from the ECS only"

  ingress {
    protocol        = "tcp"
    from_port       = 5432
    to_port         = 5432
    cidr_blocks     = ["0.0.0.0/0"]
    security_groups = [aws_security_group.ecs_tasks.id]
  }
  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

data "aws_secretsmanager_secret_version" "rds_password" {
  secret_id = "RDSPostgresPassword"
}

output "postgres_db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
