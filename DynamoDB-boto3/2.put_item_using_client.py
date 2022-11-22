import boto3 as b3
from pprint import pprint

def put_item(table_name,item):
	try:
		session = b3.session.Session(profile_name='Diana')

		db = session.client(service_name='dynamodb')

		response = db.put_item(TableName=table_name,Item=item)

		pprint(response)
		print('Item inserted successfully.')

	except Exception as e:
		print(e)


table_name = 'Employee'
item = {
	'emp_id':{
		'N':'2'
	},
	'Name':{
		'S':'Jason'
	},
	'Email':{
		'S':'Jason@mail.com'
	}
}

put_item(table_name,item)