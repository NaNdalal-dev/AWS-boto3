import boto3 as b3
from pprint import pprint

def scan_data(table_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		db = session.resource(service_name='dynamodb')

		table = db.Table(table_name)
		
		response = table.scan()

		return response['Items']

	except Exception as e:
		print(e)


table = 'Employee'

pprint(scan_data(table))