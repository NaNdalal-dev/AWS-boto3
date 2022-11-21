import boto3 as b3
from pprint import pprint

def add_user_to_group(user_name, group_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response=iam.add_user_to_group(
			UserName=user_name,
			GroupName=group_name
			)
		pprint(response)
		print(f'{user_name} added to {group_name} group.')
	except Exception as e:
		print(e)

#This user was created in create_user.py
user_name = 'elon-musk'

#This group was created in create_group.py
group_name = 'EC2-Admins'

add_user_to_group(user_name, group_name)

