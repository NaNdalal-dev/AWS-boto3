import boto3 as b3

#Give Credentials

session = b3.session.Session(profile_name='Diana')

#Select SNS topic
sns = session.resource(service_name='sns')

#Create a topic

topic = input('Enter Topic Name:')

topic = sns.create_topic(Name=topic)

print("Topic Created Successfully")
print(topic)