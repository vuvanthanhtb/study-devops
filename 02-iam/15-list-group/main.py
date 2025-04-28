import boto3
from pprint import pprint


def list_groups():
  iam_client = boto3.client('iam')
  try:
    response = iam_client.list_groups()
    pprint(response["Groups"])
  except Exception as e:
    print(f"Error list groups: {str(e)}")


if __name__ == "__main__":
  list_groups()
