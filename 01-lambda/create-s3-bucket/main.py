import json
import boto3
import random


def lambda_handler(event, context):
  s3 = boto3.client('s3')
  random_suffix = ''.join(str(random.randint(0, 100)) for _ in range(6))
  default_bucket_name = f"thanhvv-bucket-{random_suffix}"
  bucket_name = event.get('bucket_name', default_bucket_name)

  try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'
        },
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Bucket {bucket_name} created successfully!',
            'location': response['Location']
        })
    }

  except Exception as e:
    return {
        'statusCode': 500,
        'body': json.dumps({
            'message': f'Error creating bucket {bucket_name}: {str(e)}'
        })
    }
