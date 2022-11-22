import boto3 as b3
from pprint import pprint


session = b3.session.Session(profile_name='Diana')

db = session.resource(service_name='dynamodb')

#batch get item get upto 100 items from 1 or more tables

response = db.batch_get_item(
	RequestItems = {
			'Employee':{
				'Keys':[
					{
						'emp_id':1,
					},
					{
						'emp_id':2,
					},
					{
						'emp_id':3,
					},
					{
						'emp_id':4,
					},
					
				]
			}
		}
	)

pprint(response['Responses']['Employee'])