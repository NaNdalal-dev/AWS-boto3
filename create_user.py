import boto3 as b3
from pprint import pprint
def create_user(UserName):
	try:
		session = b3.session.Session(profile_name='Diana')

		iam = session.client(service_name='iam')

		response = iam.create_user(UserName=UserName)

		pprint(response)
	except Exception as e:
		print(e)



create_user('elon-musk')