import boto3 as b3
from pprint import pprint

def delete_backup_table(backup_arn):
	try:
		session = b3.session.Session(profile_name='Diana')

		db = session.client(service_name='dynamodb')

		response =	db.delete_backup(
				BackupArn=backup_arn
			)
		print(f'Backup table deleted succesfully.')
		return response
	except Exception as e:
		print(e)

arn = 'arn:aws:dynamodb:ap-south-1:356510829473:table/Employee/backup/01669087879877-0510354e'
pprint(delete_backup_table(arn))