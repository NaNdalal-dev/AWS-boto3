import boto3 as b3
from pprint import pprint

def list_iam_users():
	session = b3.session.Session(profile_name='Diana')

	iam = session.client(service_name='iam')

	paginator = iam.get_paginator('list_users')

	for each_page in paginator.paginate():
		for each_user in each_page['Users']:
			print('User:',each_user['UserName'])
			print('ARN:',each_user['Arn'])
			print('\n')

list_iam_users()