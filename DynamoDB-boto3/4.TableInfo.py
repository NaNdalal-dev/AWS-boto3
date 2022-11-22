import boto3 as b3
from pprint import pprint

def getTableInfo(table_name):
	try:
		session = b3.session.Session(profile_name='Diana')
		db = session.client(service_name='dynamodb')

		response = db.describe_table(
			TableName=table_name
			)
		return response
	except Exception as e:
		print(e)

pprint(getTableInfo('Employee'))