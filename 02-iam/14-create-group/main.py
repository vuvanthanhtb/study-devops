import boto3
from pprint import pprint


def create_group(group_name):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.create_group(
        GroupName=group_name
    )
    pprint(response["Group"])
  except Exception as e:
    print(f"Error create group: {str(e)}")


if __name__ == "__main__":
  try:
    group_name = input("Enter group name: ")
    create_group(group_name)
  except Exception as e:
    print(f"Error: {str(e)}")
