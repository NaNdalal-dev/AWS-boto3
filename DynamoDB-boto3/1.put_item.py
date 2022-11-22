import boto3 as b3
from pprint import pprint

def put_item(item):
	try:
		session = b3.session.Session(profile_name='Diana')

		db = session.resource(service_name='dynamodb')

		table = db.Table('Employee')

		response = table.put_item(Item=item)

		pprint(response)
		print('Item inserted successfully.')

	except Exception as e:
		print(e)


item = {
	
	'emp_id':1,
	'Name':'John',
	'Email':'John@mail.com'
}

put_item(item)