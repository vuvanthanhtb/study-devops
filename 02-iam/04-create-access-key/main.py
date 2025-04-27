import boto3
from pprint import pprint


def create_access_key(username):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.create_access_key(
        UserName=username,
    )

    result = {
        'AccessKeyId': response['AccessKey']['AccessKeyId'],
        'SecretAccessKey': response['AccessKey']['SecretAccessKey'],
    }

    pprint(result)
  except Exception as e:
    print(f"Error creating access key: {str(e)}")


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    create_access_key(username)
  except Exception as e:
    print(f"Error: {str(e)}")
