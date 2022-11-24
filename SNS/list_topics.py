import boto3 as b3 

session = b3.session.Session(profile_name='Diana')

sns = session.resource(service_name='sns')

print('List of Topics:')
for each_topic in sns.topics.all():
	print(each_topic.arn.split(':')[-1])