#Create a cloudwatch rule to trigger this function at 9AM IST(MON-FRI)

'''
Cron expression(UTC)
30 3 ? * * 2022
'''


import json
import boto3 as b3
def lambda_handler(event, context):
    # TODO implement
    ec2 = b3.resource('ec2')
    my_filter = {'Name':'tag:Name','Values':['linux1']}
    for i in ec2.instances.filter(Filters=[my_filter]):
        print(i.start())
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda instance!')
    }
