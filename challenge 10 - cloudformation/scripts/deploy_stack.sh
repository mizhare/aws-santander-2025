#!/bin/bash

REGION="us-east-1"
TEMPLATE_FILE="../templates/data-lake-stack.yaml"
VPC_ID="vpc-00fade6970aeb3218"
SUBNET_ID="subnet-0caaa1427d90701a3"

# Stack name unique to avoid conflicts
STACK_NAME="DataLakeStack-$(date +%s)"

echo "Deploying CloudFormation stack: $STACK_NAME"

aws cloudformation create-stack \
  --stack-name $STACK_NAME \
  --template-body file://$TEMPLATE_FILE \
  --parameters \
      ParameterKey=VpcId,ParameterValue=$VPC_ID \
      ParameterKey=SubnetId,ParameterValue=$SUBNET_ID \
  --region $REGION

echo "Waiting for stack creation to complete..."
aws cloudformation wait stack-create-complete \
  --stack-name $STACK_NAME \
  --region $REGION

echo "Stack $STACK_NAME deployed successfully!"

echo "Fetching stack outputs..."
aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --region $REGION \
  --query "Stacks[0].Outputs" \
  --output table
