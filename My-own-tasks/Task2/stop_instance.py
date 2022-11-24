#Create a cloudwatch rule to trigger this function at 6PM IST(MON-FRI)

'''
Cron expression(UTC)
30 12 ? * * 2022
'''


import json
import boto3 as b3

def lambda_handler(event, context):
    ec2 = b3.resource('ec2')
    my_filters = {'Name':'tag:Name','Values':['linux1']}
    
    for ins in ec2.instances.filter(Filters=[my_filters]):
        print(ins.stop())
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
