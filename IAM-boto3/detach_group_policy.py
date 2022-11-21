import boto3 as b3
from pprint import pprint

def detach_group_policy(group_name, arn):
	try:
		session = b3.session.Session(profile_name='Diana')
		iam = session.client(service_name='iam')

		response = iam.detach_group_policy(
				GroupName=group_name,
				PolicyArn=arn
			)

		pprint(response)
		print('Policy detached successfully.')

	except Exception as e:
		print(e)


#This group was created in create_group.py
group_name = 'S3-Admins'
arn = 'arn:aws:iam::aws:policy/AmazonS3FullAccess'
detach_group_policy(group_name, arn)