import boto3 as b3
from pprint import pprint

def updateUserName(old_name,new_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response=iam.update_user(
			UserName=old_name,
			NewUserName=new_name
			)

		pprint(response)

	except Exception as e:
		print(e)
updateUserName('elon-musk','tim-cook')