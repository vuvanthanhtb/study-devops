import boto3


def create_user(username):
  iam_client = boto3.client('iam')
  try:
    response = iam_client.create_user(
        UserName=username,
    )

    return response
  except Exception as e:
    print(f"Error creating user: {str(e)}")
    return None


if __name__ == "__main__":
  try:
    username = input("Enter username: ")
    if create_user(username):
      print("User created successfully!")

  except Exception as e:
    print(f"Error: {str(e)}")
  except KeyboardInterrupt:
    print("Exiting...")

