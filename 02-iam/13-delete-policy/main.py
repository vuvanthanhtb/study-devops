import boto3
from pprint import pprint


def delete_policy(policy_arn):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.delete_policy(
        PolicyArn=policy_arn
    )
    pprint(response["ResponseMetadata"])
  except Exception as e:
    print(f"Error delete policy: {str(e)}")


if __name__ == "__main__":
  try:
    policy_arn = input("Enter policy ARN: ")
    delete_policy(policy_arn)
  except Exception as e:
    print(f"Error: {str(e)}")
