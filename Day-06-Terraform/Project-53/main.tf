data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name    = "${var.project_name}-vpc"
    Project = var.project_name
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name    = "${var.project_name}-igw"
    Project = var.project_name
  }
}

locals {
  subnets = {
    public_a  = { cidr = "10.53.1.0/24", az_index = 0, tier = "public" }
    public_b  = { cidr = "10.53.2.0/24", az_index = 1, tier = "public" }
    private_a = { cidr = "10.53.11.0/24", az_index = 0, tier = "private" }
    private_b = { cidr = "10.53.12.0/24", az_index = 1, tier = "private" }
  }
}

resource "aws_subnet" "this" {
  for_each = local.subnets

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value.cidr
  availability_zone       = data.aws_availability_zones.available.names[each.value.az_index]
  map_public_ip_on_launch = each.value.tier == "public"

  tags = {
    Name    = "${var.project_name}-${replace(each.key, "_", "-")}"
    Project = var.project_name
    Tier    = each.value.tier
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name    = "${var.project_name}-public-rt"
    Project = var.project_name
  }
}

resource "aws_route_table_association" "public" {
  for_each = {
    public_a = aws_subnet.this["public_a"].id
    public_b = aws_subnet.this["public_b"].id
  }

  subnet_id      = each.value
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table" "private" {
  for_each = {
    private_a = aws_subnet.this["private_a"].id
    private_b = aws_subnet.this["private_b"].id
  }

  vpc_id = aws_vpc.main.id

  tags = {
    Name    = "${var.project_name}-${replace(each.key, "_", "-")}-rt"
    Project = var.project_name
  }
}

resource "aws_route_table_association" "private" {
  for_each = aws_route_table.private

  subnet_id      = aws_subnet.this[each.key].id
  route_table_id = each.value.id
}
