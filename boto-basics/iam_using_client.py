import boto3

user = boto3.session.Session(profile_name='Diana')

iam = user.client('iam')

for each_user in iam.list_users()['Users']:
	print(each_user['UserName'])