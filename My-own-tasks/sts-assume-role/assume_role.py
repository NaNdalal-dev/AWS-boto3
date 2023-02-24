import boto3

session = boto3.Session(profile_name="elon-musk")

sts = session.client("sts")

response = sts.assume_role(
    RoleArn="arn:aws:iam::464498422823:role/Ec2-switch-role",
    RoleSessionName="Ec2-session"
)

print(response)