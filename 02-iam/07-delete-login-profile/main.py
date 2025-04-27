import boto3
from pprint import pprint


def delete_login_profile(username):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.delete_login_profile(
        UserName=username,
    )

    pprint(response["ResponseMetadata"])
  except Exception as e:
    print(f"Error deleting login profile: {str(e)}")


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    delete_login_profile(username)
  except Exception as e:
    print(f"Error: {str(e)}")
