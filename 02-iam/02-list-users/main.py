import boto3


def list_users():
  iam_client = boto3.client('iam')
  try:
    response = iam_client.list_users()
    for user in response['Users']:
      print(f"User: {user['UserName']} - ARN: {user['Arn']}")
  except Exception as e:
    print(f"Error list users: {str(e)}")


if __name__ == "__main__":
  list_users()
