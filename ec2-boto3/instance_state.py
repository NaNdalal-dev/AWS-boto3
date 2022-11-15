import boto3

ec2 = boto3.resource('ec2')

while True:
	ins_id = input('Enter Instance ID:')
	instance = ec2.Instance(ins_id)
	print("1.Start Instance.")
	print("2.Stop Instance.")
	print("3.Terminate Instance.")
	print("4.Exit.")
	option = input("Enter your choice:")

	if option == '1':
		print("Starting the instance...")
		instance.start()
		instance.wait_until_running()
		print(f"Instance ({ins_id}) started successfully.")
		print("Check the console to verify.")
	elif option == '2':
		print("Stopping the instance...")
		instance.stop()
		print(f"Instance ({ins_id}) stopped successfully.")
		print("Check the console to verify.")
	elif option == '3':
		print("Terminating the instance...")
		instance.terminate()
		print(f"Instance ({ins_id}) terminated successfully.")
		print("Check the console to verify.")
	elif option == '4':
		print("Program Stopped.")
		exit()
	else:
		print("Invalid Option")
	print("==========================")