import boto3 as b3
from pprint import pprint
session = b3.session.Session(profile_name='Diana')
ec2 = session.client(service_name='ec2',region_name='ap-south-1')

for each in ec2.describe_instances()['Reservations']:
	for each_instance in (each['Instances']):
		print(each_instance)