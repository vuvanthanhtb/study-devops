import boto3
from pprint import pprint


def attach_user_policy(username, policy_arn):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    pprint(response["ResponseMetadata"])
  except Exception as e:
    print(f"Error attach user policy: {str(e)}")


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    policy_arn = input("Enter policy ARN: ")
    attach_user_policy(username, policy_arn)
  except Exception as e:
    print(f"Error: {str(e)}")
