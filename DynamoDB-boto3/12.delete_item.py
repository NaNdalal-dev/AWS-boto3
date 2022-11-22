import boto3 as b3
from pprint import pprint

def delete_item(emp_id):
	try:
		session = b3.session.Session(profile_name='Diana')
		db = session.resource(service_name='dynamodb')

		table = db.Table('Employee')

		response = table.delete_item(
				Key={
					'emp_id':emp_id

				}  
			)
		print('Item deleted successfully.')
		return response

	except Exception as e:
		print(e)

#pprint(delete_item(9))
pprint(delete_item(8))