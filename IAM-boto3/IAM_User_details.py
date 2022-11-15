import boto3 as b3
console = b3.session.Session(profile_name='Diana')

iam = console.resource(service_name='iam')

for each_user in iam.users.all():
	print(each_user.user_id,each_user.user_name,each_user.arn)