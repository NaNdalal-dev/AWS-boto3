import boto3 as b3
from pprint import pprint


def create_policy(arn, userName):
	session = b3.session.Session(profile_name='Diana')
	iam = session.client(service_name='iam')

	response = iam.attach_user_policy(
		UserName=userName,
		PolicyArn=arn
		)
	return response
	

#This Policy was created in create_admin+policy.py	
arn = 'arn:aws:iam::356510829473:policy/AdminAccess2'

#This user was created in create_user.py
user = 'elon-musk'

pprint(create_policy(arn, user))