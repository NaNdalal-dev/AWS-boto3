import boto3 as b3
from pprint import pprint

def delete_user_from_group(group_name, user_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.resource(service_name='iam')

		group = iam.Group(group_name)

		response = group.remove_user(UserName=user_name)

		pprint(response)
		print(f'User {user_name} successfully removed from {group_name}')

	except Exception as e:
		print(e)

#This group was created in create_group.py
group_name='EC2-Admins'

#This user was created in create_user.py
iam_user='elon-musk'

delete_user_from_group(group_name, iam_user)

