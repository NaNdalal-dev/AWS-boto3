import boto3 as b3
from pprint import pprint

def deactivate_credential(user_name, accessid):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response = iam.update_access_key(
			AccessKeyId=accessid,
			UserName=user_name,
			Status='Inactive'
			)
		pprint(response)

	except Exception as e:
		print(e)


#This user was created in create_user.py
iam_user='elon-musk'
accessid = 'AKIAVGANTROQR2QK6SGJ'

deactivate_credential(iam_user,accessid)
