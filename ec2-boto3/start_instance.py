import boto3
#User = Default
#Region = ap-south-1(mumbai)

ec2 =boto3.resource('ec2')

ins_id = input("Enter Instance ID:")

ins = ec2.Instance(ins_id)

ins.start()