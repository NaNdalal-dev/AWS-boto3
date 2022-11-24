
import boto3 as b3 

session = b3.session.Session(profile_name='Diana')

sns = session.resource(service_name='sns')

arn='arn:aws:sns:ap-south-1:356510829473:mail-notifier2'

topic = sns.Topic(arn)

topic.delete()

print(arn,' Deleted')