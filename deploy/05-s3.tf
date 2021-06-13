resource "aws_s3_bucket" "python_app" {
  bucket        = var.app_name
  acl           = "private"
  force_destroy = true

}