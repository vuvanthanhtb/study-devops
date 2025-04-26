import boto3
import json


def lambda_handler(event, context):
  try:
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = []
    for bucket in response['Buckets']:
      buckets.append(bucket['Name'])

    return {
        'statusCode': 200,
        'body': json.dumps({
            'buckets': buckets
        })
    }
  except Exception as e:
    return {
        'statusCode': 500,
        'body': json.dumps({
            'message': f'Error listing buckets: {str(e)}'
        })
    }
