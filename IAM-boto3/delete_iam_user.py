import boto3 as b3
from pprint import pprint

def delete_user(user_name):
	#Note
	#Before deleting a user maker user to delete accesskeyid and attached policies.
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		iam.delete_user(UserName=user_name)
		print(f'User {user_name} deleted.')
	except Exception as e:
		print(e)

delete_user('test')