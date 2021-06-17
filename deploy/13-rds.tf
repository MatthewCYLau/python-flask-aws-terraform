resource "aws_db_instance" "postgres" {
  allocated_storage    = 10
  engine               = "postgres"
  engine_version       = "9.6.20"
  instance_class       = "db.t3.micro"
  name                 = "flaskdb"
  username             = "foo"
  password             = "barbarbar"
  skip_final_snapshot  = true
  db_subnet_group_name = aws_db_subnet_group.postgres.name
}

resource "aws_db_subnet_group" "postgres" {
  name       = "postgres-subnet"
  subnet_ids = [aws_subnet.pub_subnet.id, aws_subnet.pub_subnet2.id]

  tags = {
    Name = "PostgreSQL DB subnet group"
  }
}


output "postgres_db_endpoint" {
  value = aws_db_instance.postgres.endpoint
}
