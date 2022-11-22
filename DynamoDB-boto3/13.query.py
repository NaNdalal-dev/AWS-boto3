import boto3 as b3
from pprint import pprint
from boto3.dynamodb.conditions import Key

def query_table(key, value):
	if value.isdigit():
		value=int(value)
	try:
		session = b3.session.Session(profile_name='Diana')
		db = session.resource(service_name='dynamodb')

		table = db.Table('Employee')

		response = table.query(
			KeyConditionExpression=Key(key).eq(value)
			)
		return response['Items']
	except Exception as e:
		print(e)

key = 'emp_id'
value = input('Enter Item Value:')

pprint(query_table(key,value))