import boto3 as b3

session = b3.session.Session(profile_name='Diana')

iam = session.resource(service_name='iam')

groups = iam.groups.all()

for each_group in groups:
	print('Group ID:',each_group.group_id)
	print('Group Name:',each_group.group_name)
	print('Users:')
	for each_user in each_group.users.all():
		print(each_user.name)
	print()