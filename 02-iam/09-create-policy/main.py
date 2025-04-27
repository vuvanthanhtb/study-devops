import boto3
from pprint import pprint


def policy_document():
  json_file_input = input("Enter json file name: ") + ".json"
  with open(json_file_input, "r") as file:
    content = file.read()
  return content


def create_policy(policy_name, policy_document):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.create_policy(
        PolicyName=policy_name,
        PolicyDocument=policy_document,
        Description='demo policy for s3 access'
    )

    pprint(response["Policy"])
  except Exception as e:
    print(f"Error creating policy: {str(e)}")


if __name__ == "__main__":
  try:
    policy_name = input("Enter policy name: ")
    policy_document = policy_document()
    create_policy(policy_name, policy_document)
  except Exception as e:
    print(f"Error: {str(e)}")
