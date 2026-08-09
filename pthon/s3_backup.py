"""
Script to backup files to an AWS s3
 """
import boto3 # library to interact with AWS services using python
s3 = boto3.resource("s3") # creating a resource object for s3
def show_buckets(s3):
    print(s3.buckets.all())