#!/bin/bash
##########
#author :vijay
#date:04-04-2024
#version:v1
##################
#this script will report the aws resource usage
#aws S3
#aws EC2
#aws IAM USERS
set -x
echo "print list of s3 buckets"
aws s3 ls
echo "print list of ec2 instances"
aws ec2 describe-instances |jq '.Reservation[].Instances[].InstanceId'
echo "print list of lambda functions"
aws lambda list-functions
echo "print list of iam users"
aws iam list-users
