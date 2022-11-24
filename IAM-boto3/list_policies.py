import boto3 as b3
from pprint import pprint

def list_policies(scope):

	session = b3.session.Session(profile_name='Diana')

	iam = session.client(service_name='iam')

	policies = iam.get_paginator('list_policies')
	count = 1
	print(f'Policies under {scope}:\n')
	for response in policies.paginate(Scope=scope):
		for each_policy in response['Policies']:
			print('Policy Name:',each_policy['PolicyName'])
			print('Policy ARN:',each_policy['Arn'])
			print()
			count+=1
	print(f'Total policies under {scope}:',count)
list_policies('Local')

list_policies('AWS')