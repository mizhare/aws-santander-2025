## AWS Data Lake CloudFormation Deployment

This project demonstrates how to create a simple Data Lake environment on AWS using CloudFormation.
It sets up an S3 bucket for storing data, an EC2 instance for processing, and a security group to allow access.

The included deployment script automates the stack creation and shows the outputs once ready.
This setup is perfect for experimenting with AWS infrastructure and learning CloudFormation in a hands-on way.

How to Use:

1. Make sure you have a KeyPair in the same region as your VPC and Subnet.

2. Update the VPC and Subnet IDs in the deploy_stack.sh script.

3. Run the deployment:

```bash
chmod +x deploy_stack.sh
./deploy_stack.sh
```
