import boto3 as b3

session = b3.session.Session(profile_name='root')

iam = session.resource(service_name='iam')

user = iam.User('Diana')

print(user.user_id,user.user_name,user.arn)