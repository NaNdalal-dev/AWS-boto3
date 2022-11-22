import boto3 as b3
from pprint import pprint

def create_backup_table(table_name,backup_name):
	try:
		session = b3.session.Session(profile_name='Diana')

		db = session.client(service_name='dynamodb')

		response =	db.create_backup(
				TableName=table_name,
				BackupName=backup_name
			)
		print(f'Backup for {table_name} table created succesfully.')
		return response
	except Exception as e:
		print(e)

table = 'Employee'
backup = table+'_backup'

pprint(create_backup_table(table, backup))