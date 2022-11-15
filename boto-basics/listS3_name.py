import boto3

user = boto3.session.Session(profile_name='Diana')

s3 = user.resource('s3')

for each_buckets in s3.buckets.all():
	print(each_buckets.name)