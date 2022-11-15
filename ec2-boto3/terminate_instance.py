import boto3

ins_id = input("Enter Instance ID:")

ec2 = boto3.resource('ec2')

instance = ec2.Instance(ins_id)

instance.terminate()