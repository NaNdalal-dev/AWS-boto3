import boto3

#User = Default
#Region = ap-south-1(mumbai)
ins_id = input("Enter Instance ID:")

ec2 = boto3.resource('ec2')

instance = ec2.Instance(ins_id)

instance.stop()