import boto3 as b3
from pprint import pprint
import json

def create_policy():
	policy = {
		"Version":"2012-10-17",
		"Statement":[
			{
				"Effect":"Allow",
				"Action":"*",
				"Resource":"*"
			}
		]

	}

	session = b3.session.Session(profile_name='Diana')

	iam = session.client(service_name='iam')

	response=iam.create_policy(
		PolicyName='AdminAccess2',
		PolicyDocument=json.dumps(policy)

		)

	pprint(response)

create_policy()
