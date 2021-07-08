import boto3
import os
import credentials as cs
import pandas as pd

# session = boto3.Session(aws_access_key_id=cs.aws_access_key_id, aws_secret_access_key = cs.aws_secret_access_key)
# s3 = session.resource(service_name = 's3')

# obj = s3.get_object(Bucket='mybucketritesh', Key='test_file')
# initial_df = pd.read_csv(io.BytesIO(obj['Body'].read()))
#for bucket in s3.buckets.all():
   #print(bucket.name)

s3_client = boto3.client('s3', aws_access_key_id=cs.aws_access_key_id, aws_secret_access_key = cs.aws_secret_access_key )

response = s3_client.get_object(Bucket='mybucketritesh', Key='test_file.csv')
status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

if status == 200:
    print(f"Successful S3 get_object response. Status - {status}")
    df = pd.read_csv(response.get("Body"))
    print(df)
else:
    print(f"Unsuccessful S3 get_object response. Status - {status}")



