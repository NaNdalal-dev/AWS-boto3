import boto3 as b3
from pprint import pprint

session = b3.session.Session(profile_name='Diana')

db = session.client(service_name='dynamodb')

response = db.get_item(
		TableName='Employee',
		Key={
			'emp_id':{
				'N':'9'
			}

		}
	)

print(response['Item'])