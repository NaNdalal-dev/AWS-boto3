import boto3 

ec2 = boto3.resource(service_name='ec2')

instances = ec2.instances.all()

print([i.id for i in instances])

#Get limited number of instance ids
# print([i.id for i in instances.limit(1)])

#Filter instance
f1 = {"Name":"vpc-id", "Values":["vpc-0b7db36f6986aa150"]}

print([i.id for i in instances.filter(Filters=[f1])])