import boto3 as b3
from pprint import pprint

def create_group(group_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response = iam.create_group(GroupName=group_name)
		return response
	except Exception as e:
		print(e)


groups = ['EC2-Admins', 'S3-Admins']

for each_group in groups:
	if create_group(each_group) is not None:
		print(each_group,'group created.')
