import boto3


account = boto3.client('sts')

print(account.get_caller_identity())