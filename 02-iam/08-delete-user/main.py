import boto3
from pprint import pprint


def delete_user(username):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.delete_user(
        UserName=username,
    )

    pprint(response["ResponseMetadata"])
  except Exception as e:
    print(f"Error deleting user: {str(e)}")


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    delete_user(username)
  except Exception as e:
    print(f"Error: {str(e)}")
