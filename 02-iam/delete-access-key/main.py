import boto3
from pprint import pprint


def delete_access_key(username, access_key_id):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.delete_access_key(
        UserName=username,
        AccessKeyId=access_key_id,
    )

    pprint(response)
  except Exception as e:
    print(f"Error delete access key: {str(e)}")


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    access_key_id = input("Enter access key id: ")
    delete_access_key(username, access_key_id)
  except Exception as e:
    print(f"Error: {str(e)}")
