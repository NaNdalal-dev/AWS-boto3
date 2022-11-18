import boto3 as b3 

session = b3.session.Session(profile_name='Diana')

sns = session.resource(service_name='sns')

endpoint = 'dnandalal7@gmail.com'
arn = 'arn:aws:sns:ap-south-1:356510829473:mail-notifier2'

protocol='email'


topic = sns.Topic(arn)

topic.publish(Message='Hello World')