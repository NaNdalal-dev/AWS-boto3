import boto3

#User = Default
#Region = ap-south-1(mumbai)

iam = boto3.client('iam')
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

print("IAM-Users:")
for each_user in iam.list_users()['Users']:
	print(each_user['UserName'])
print('------------------------------')
print("EC2 Instance Ids:")
for each_val in ec2.describe_instances()['Reservations']:
	for each_id in each_val['Instances']:
		print(each_id['InstanceId'])
print('------------------------------')
print("Buckets:")
for each_bucket in s3.list_buckets()['Buckets']:
	bucket_name = each_bucket['Name']
	print(bucket_name)
	print("---")
	print(f"Objects of {bucket_name}:")
	objects = s3.list_objects(Bucket=bucket_name)
	for each_object_name in objects['Contents']:
		print(each_object_name['Key'])
'''
Sample Output:

IAM-Users:
Diana
------------------------------
EC2 Instance Ids:
i-077b48e3a9e69439e
i-01755e7852ac6d8a2
------------------------------
Buckets:
stack221
---
Objects of stack221:
Gaming-PNG-Photo.png
disney-plus-logo-0.png
'''