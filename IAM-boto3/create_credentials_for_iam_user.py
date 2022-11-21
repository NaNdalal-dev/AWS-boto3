import boto3 as b3
from pprint import pprint

def create_credentials(user_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response = iam.create_access_key(
			UserName=user_name
			)
		pprint(response)

	except Exception as e:
		print(e)


#This user was created in create_user.py
iam_user='elon-musk'

create_credentials(iam_user)
