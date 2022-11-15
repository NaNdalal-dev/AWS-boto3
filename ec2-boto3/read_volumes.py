import boto3

ec2 = boto3.resource('ec2')

volumes = ec2.volumes

unused_volumes = volumes.all()#.filter(Filters=fil)

for vol in unused_volumes:
	
	if vol.tags is None and vol.state == 'available':
		print('Deleting unused and untagged volumes')
		vol.delete()

print('Deleted the volumes.')

# Using filter method
# fil ={'Name':'status','Values':['available']}
# unused_volumes = volumes.filter(Filters=[fil])

# for i in unused_volumes:
# 	print(i)