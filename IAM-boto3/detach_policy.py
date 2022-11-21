import boto3 as b3
from pprint import pprint

def detach_policy(arn, userName):
	session = b3.session.Session(profile_name='Diana')
	iam = session.client(service_name='iam')

	response = iam.detach_user_policy(
		UserName=userName,
		PolicyArn=arn
		)
	return response

#This Policy was created in create_admin_policy.py	
arn = 'arn:aws:iam::356510829473:policy/AdminAccess2'

#This user was created in create_user.py
user = 'elon-musk'

pprint(detach_policy(arn, user))