# Provider configuration for AWS
provider "aws" {
  region = "us-east-1"
}

# Create a VPC for network isolation
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "fastapi-vpc"
  }
}

# Create a subnet for EC2 instance
resource "aws_subnet" "subnet" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "FastAPI-Subnet"
  }
}

# Create a security group to allow traffic on port 80
resource "aws_security_group" "fastapi_sg" {
  name        = "fastapi_security_group"
  description = "Allow all inbound traffic to FastAPI app"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 instance to serve FastAPI app
resource "aws_instance" "fastapi_instance" {
  ami             = "ami-0c55b159cbfafe1f0"  # Replace with an appropriate AMI (Amazon Linux or Ubuntu)
  instance_type   = "t2.micro"
  subnet_id       = aws_subnet.subnet.id
  security_groups = [aws_security_group.fastapi_sg.name]

  tags = {
    Name = "FastAPI-Instance"
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo yum update -y
              sudo yum install python3 -y
              sudo pip3 install fastapi uvicorn
              echo "Starting FastAPI app..."
              nohup uvicorn main:app --host 0.0.0.0 --port 80 &
              EOF

  lifecycle {
    create_before_destroy = true
  }
}

# Elastic IP for static IP address (optional)
resource "aws_eip" "fastapi_eip" {
  instance = aws_instance.fastapi_instance.id
  vpc      = true
}

# QuickSight User setup
resource "aws_quicksight_user" "fastapi_user" {
  aws_account_id = "your-aws-account-id"
  namespace      = "default"
  user_name      = "fastapi_user"
  email          = "user@example.com"
  role           = "READER"

  tags = {
    Name = "FastAPI User"
  }
}

# IAM role for QuickSight to access resources like S3
resource "aws_iam_role" "quicksight_role" {
  name               = "quicksight-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "quicksight.amazonaws.com"
        }
      },
    ]
  })
}

# IAM policy for QuickSight to interact with S3
resource "aws_iam_policy" "quicksight_policy" {
  name        = "quicksight-policy"
  description = "Allow access to QuickSight data sources"
  policy      = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = [
          "s3:GetObject",
          "s3:ListBucket"
        ]
        Resource = "arn:aws:s3:::your-bucket-name/*"
      },
      {
        Effect   = "Allow"
        Action   = "rds:DescribeDBInstances"
        Resource = "*"
      },
    ]
  })
}

# Attach the IAM policy to the role
resource "aws_iam_role_policy_attachment" "quicksight_attach" {
  policy_arn = aws_iam_policy.quicksight_policy.arn
  role       = aws_iam_role.quicksight_role.name
}

# Create an S3 bucket to store data for FastAPI or QuickSight
resource "aws_s3_bucket" "fastapi_data" {
  bucket = "fastapi-data-bucket"
  acl    = "private"

  tags = {
    Name        = "FastAPI Data Bucket"
    Environment = "Production"
  }
}
