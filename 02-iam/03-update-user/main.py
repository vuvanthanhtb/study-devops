from pprint import pprint
import boto3


def update_user(old_username, new_username):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.update_user(
        UserName=old_username,
        NewUserName=new_username,
    )

    pprint(response)
  except Exception as e:
    pprint(f"Error update user: {str(e)}")
    return None


if __name__ == "__main__":
  try:
    old_username = input("Enter old username: ")
    new_username = input("Enter new username: ")
    update_user(old_username, new_username)
  except Exception as e:
    pprint(f"Error: {str(e)}")
