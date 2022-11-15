import json
import boto3 as b3

def lambda_handler(event, context):
    # TODO implement
    ec2 = b3.resource('ec2')
    my_filter = {'Name':'tag:Name','Values':['linux1']}
    #Starting the linux1 instance(s) 

    for ins in ec2.instances.filter(Filters=[my_filter]):
        print(ins.start())

    #Ignore
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda instance!')
    }