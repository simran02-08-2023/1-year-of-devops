import boto3
s3 = boto3.resource("s3", region_name="eu-west-1")
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3):
    s3.create_bucket(
        Bucket="python-for-devops-simran",
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    )
    print("Bucket created successfully")

show_buckets(s3)
create_bucket(s3)