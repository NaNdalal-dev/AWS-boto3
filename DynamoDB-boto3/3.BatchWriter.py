import boto3 as b3
from pprint import pprint

session = b3.session.Session(profile_name='Diana')
db = session.resource(service_name='dynamodb')

table = db.Table('Employee')

#Batch writer allows to insert upto 25 items into table
with table.batch_writer() as batch:
	for i in range(3,10):
		batch.put_item(
			Item = {
					'emp_id':i,
					'Name':f'User{i}',
					'Email':f'User{i}@mail.com'
				}
			)
	print('Items inserted.')
