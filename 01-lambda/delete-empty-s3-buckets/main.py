import json
import boto3


def delete_empty_s3_buckets(event, context):
  s3_client = boto3.client('s3')
  try:
    bucket_name = event.get('bucket_name')
    s3_client.delete_bucket(Bucket=bucket_name)
    return {
        'statusCode': 200,
        'body': f"Bucket {bucket_name} deleted successfully!"
    }
  except Exception as e:
    return {
        'statusCode': 500,
        'body': json.dumps({
            'message': f'Error deleting buckets: {str(e)}'
        })
    }
