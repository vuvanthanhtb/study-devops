import boto3
from pprint import pprint


def list_policies(scope = "AWS", only_attached = False, policy_usage_filter = "PermissionsPolicy"):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.list_policies(
        Scope=scope,
        OnlyAttached=only_attached,
        PolicyUsageFilter=policy_usage_filter,
    )
    pprint(
        [f"{policy['PolicyId']}::{policy['PolicyName']}" for policy in response["Policies"]])
  except Exception as e:
    print(f"Error listing policies: {str(e)}")


if __name__ == "__main__":
  try:
    scope = input("Enter scope: ")
    list_policies(scope)
  except Exception as e:
    print(f"Error: {str(e)}")
