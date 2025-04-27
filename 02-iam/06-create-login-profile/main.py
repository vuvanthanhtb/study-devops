import boto3
from pprint import pprint


def create_login_profile(username, password=None, is_require=False):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.create_login_profile(
        UserName=username,
        Password=password,
        PasswordResetRequired=is_require
    )

    pprint(response["LoginProfile"])
  except Exception as e:
    pprint(f"Error creating login profile: {str(e)}")


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    password = input("Enter password: ")
    create_login_profile(username, password)
  except Exception as e:
    pprint(f"Error: {str(e)}")
