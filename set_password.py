import boto3 as b3
from pprint import pprint

def create_login(user_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response = iam.create_login_profile(
			UserName=user_name,
			Password='',
			PasswordResetRequired=False
			)

		print('password is set.')

	except Exception as e:
		print(e)

#This user was created in create_user.py
iam_user='elon-musk'

create_login(iam_user)