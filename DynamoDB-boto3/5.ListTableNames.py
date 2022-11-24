import boto3 as b3
from pprint import pprint

def list_tables():
	try:
		session = b3.session.Session(profile_name='Diana')
		db = session.client(service_name='dynamodb')

		response = db.list_tables()

		return response['TableNames']
	except Exception as e:
		print(e)

print(list_tables())