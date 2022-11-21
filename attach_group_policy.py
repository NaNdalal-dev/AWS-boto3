import boto3 as b3
from pprint import pprint

def attach_group_policy(group_name, arn):
	session = b3.session.Session(profile_name='Diana')

	iam = session.client(service_name='iam')

	response = iam.attach_group_policy(
			GroupName=group_name,
			PolicyArn=arn
		)
	pprint(response)

#These groups were created in create_group.py file 
groups_arns = {
	'EC2-Admins':'arn:aws:iam::aws:policy/AmazonEC2FullAccess', 
	'S3-Admins':'arn:aws:iam::aws:policy/AmazonS3FullAccess'
	}


for group,arn in groups_arns.items():
	# print(group,arn)
	attach_group_policy(group, arn)
	print('Policy attached to',group)
