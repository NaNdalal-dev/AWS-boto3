import boto3

user = boto3.session.Session(profile_name='Diana')

iam = user.resource('iam')

for each_user in iam.users.all():
	print(each_user.name)