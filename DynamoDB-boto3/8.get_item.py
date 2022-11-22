import boto3 as b3
from pprint import pprint


session = b3.session.Session(profile_name='Diana')

db = session.resource(service_name='dynamodb')

table = db.Table('Employee')

#Get item gets only 1 item from table
for i in range(1,10):
	response = table.get_item(
			Key = {
				"emp_id":i

			}
		)

	pprint(response['Item'])