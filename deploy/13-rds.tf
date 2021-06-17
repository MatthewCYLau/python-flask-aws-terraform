resource "aws_db_instance" "postgres" {
  allocated_storage    = 10
  engine               = "postgres"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  name                 = "flaskdb"
  username             = "foo"
  password             = "bar"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}