import os
import webbrowser
import getpass
password = getpass.getpass("Please Enter Your Password: ")
if password != "PPSS":
	print("Password Incorrect....")
	print("Thanks for using our menu system\n")
	print("Created by Prabhjeet, Pallavi, Sadiya, Sourabh")
	exit()
else:
	while True:
		os.system("clear")
		os.system("tput setaf 6")
		print("-----------------------------------------------------Welcome to Menu Program---------------------------------------------------")

		os.system("tput setaf 7")
		a = input("""Tell me sir you want to work on ->

Type "hadoop"-> to go to the hadoop
Type "create website" -> to go to the webpage
Type "rhel" -> to go to the rhel8 commands
Type "docker" -> to go to the container technology's product
Type "yum" -> to configure and use the software setup
Type "aws" -> to go to the aws program
Type "exit" -> to close the program\n\n""")

		if a == "hadoop":
			while True:
				os.system("clear")
				os.system("tput setaf 6")
				print("\t\t\t\t\tYou are now working on Apache Hadoop")
				os.system("tput setaf 7")
				b = int(input("""Press 1 to work on Name Node 
Press 2 to work on Data Node
Press 3 to work on an client
Press 4 to check your number of data node available in cluster
Press 5 Exit the Hadoop Program\n\n"""))
				if b == 1:
					os.system("tput setaf 5")
					print("You are now in name node\n")
					os.system("tput setaf 7")
					ip_address = input("Please Enter the Namenode IP: \n")
					while True:
						c = int(input("""\nPress 1 to setup hdfs file,
Press 2 to setup core.xml file,
Press 3 to format name node,
Press 4 to start Name Node,
Press 5 to check Name Node is running or not,
Press 6 to stop Name Node,
Press 7 to exit\n\n"""))
						if c == 1:
							os.system("scp name_hdfs_file.py root@{}:/root/".format(ip_address))
							os.system("ssh root@{} 'python3 name_hdfs_file.py'".format(ip_address))						
						elif c == 2:
							os.system("scp name_core_file.py root@{}:/root/".format(ip_address))
							os.system("ssh root@{} 'python3 name_core_file.py'".format(ip_address))						
						elif c == 3:
							os.system("ssh root@{} 'hadoop namenode -format'".format(ip_address))
						elif c == 4:
							os.system("ssh root@{} 'hadoop-daemon.sh start namenode'".format(ip_address))
						elif c == 5:
							os.system("ssh root@{} 'jps'".format(ip_address))
						elif c == 6:
							os.system("ssh root@{} 'hadoop-daemon.sh stop namenode'".format(ip_address))
						elif c == 7:
							break
						else:
							print("Please select correct Input from the given" )
				
				elif b == 2:
					os.system("tput setaf 3")
					print("You are now in Data Node\n")
					os.system("tput setaf 7")
					ip_address = input("Please Enter the DataNode IP: \n")
					while True:
						c = int(input("""\nPress 1 to setup hdfs file,
Press 2 to setup core.xml file,
Press 3 to start Data Node,
Press 4 to check Data Node is running or not,
Press 5 to stop Data Node,
Press 6 to exit\n\n"""))
						if c == 1:
							os.system("scp data_hdfs_file.py root@{}:/root/".format(ip_address))
							os.system("ssh root@{} 'python3 data_hdfs_file.py'".format(ip_address))
						elif c == 2:
							os.system("scp data_core_file.py root@{}:/root/".format(ip_address))
							os.system("ssh root@{} 'python3 data_core_file.py'".format(ip_address))
						elif c == 3:
							os.system("ssh root@{} 'hadoop-daemon.sh start datanode'".format(ip_address))
						elif c == 4:
							os.system("ssh root@{} 'jps'".format(ip_address))
						elif c == 5:
							os.system("ssh root@{} 'hadoop-daemon.sh stop datanode'".format(ip_address))
						elif c == 6:
							break
				elif b == 3:
					os.system("tput setaf 5")
					print("You are on an client...\n")
					os.system("tput setaf 7")
					ip_address = input("Please Enter the Client IP: \n")
					while True:
						c = int(input("""\nPress 1 to setup the hdfs file,
Press 2 to setup core file,
Press 3 to list the Client Files
Press 4 to (upload/delete) the File to an cluster
Press 5 to see the File of a client into an cluster
Press 6 to exit\n\n"""))
						if c == 1:
							os.system("scp client_hdfs.py root@{}:/root/".format(ip_address))
							os.system("ssh root@{} 'python3 client_hdfs.py'".format(ip_address))
						elif c == 2:
							os.system("scp client_core.py root@{}:/root/".format(ip_address))
							os.system("ssh root@{} 'python3 client_core.py'".format(ip_address))
						elif c == 3:
							os.system("ssh root@{} 'hadoop fs -ls /'".format(ip_address))
						elif c == 4:
							data_input = input("What do you want: (upload/delete): ")
							if data_input == "upload":
								file_name = input("Please Enter the file name with extension: ")
								os.system("ssh root@{} 'hadoop fs -put {} /'".format(ip_address,file_name))
							elif data_input == "delete":
								file_name = input("Please Enter the file name with extension: ")
								os.system("ssh root@{} 'hadoop fs -rm /{}'".format(ip_address,file_name))
							else:
								print("Not Found")
						elif c == 5:
							file_name = input("Please Enter the file name with extension: ")
							os.system("ssh root@{} hadoop fs -cat /{}".format(ip_address,file_name))
						elif c == 6:
							break
					
				elif b == 4:
					ip_address = input("Enter (Namenode/Datanode/Client IP: \n\n")
					os.system("ssh root@{} hadoop dfsadmin -report".format(ip_address))
					input()
				elif b == 5:
					break
				else:
					print("Please give correct input : Press 1 or 2 or 3only")
					input()
				print("Please Enter to continue the menu....")


		elif a == "create website":
			while True:
				import os
				os.system("clear")
				os.system("tput setaf 5")
				print("\t\t\tWelcome to the httpd configuration")
				os.system("tput setaf 7")
				print("\t\t\t------------------------\n\n")
				b = int(input("""
Press 1 : To download the httpd software
Press 2 : Start the httpd service
Press 3 : Disabled the firewall service
Press 4 : Create an website page
Press 5 : See the content of webpage
Press 6 : Deliver the content on browser
Press 7 : To Exit
\n\n"""))
				if b == 1:
					os.system("yum install httpd -y")
				elif b == 2:
					os.system("systemctl start httpd")
					os.system("systemctl enable httpd")
				elif b == 3:
					os.system("systemctl stop firewalld")
				elif b == 4:
					html_file = input("Name of an html page file: ")
					os.system("vi /var/www/html/{}.html".format(html_file))
				elif b == 5:
					html_file = input("Name of an html page file: ")
					os.system("cat /var/www/html/{}.html".format(html_file))
				elif b == 6:
					ip_address = input("Enter your IP Address: ")
					html_file = input("Enter the page name: ")
					webbrowser.open("http://{}/{}.html".format(ip_address,html_file))
				elif b == 7:
					break

				input("Please Enter to continue....")


		elif a == "rhel":
			while True:
				import os
				os.system("clear")
				os.system("tput setaf 3")
				print("\t\t\tWelcome to my linux menu")
				os.system("tput setaf 7")
				print("\t\t\t------------------------")
				print("\n\n")
				b = int(input('''Press 1 : Open the Firefox
Press 2 : See the date
Press 3 : See the current system calendar
Press 4 : See the calendar with user input
Press 5 : Check the internet connectivity of an IP
Press 6 : See the Stopped program status
Press 7 : For Continue the Stopped program
Press 8 : Make an Directory on system
Press 9 : List of the Files
Press 10 : Create an empty file
Press 11 : See the detailed List of the Files
Press 12 : Open the gedit editor
Press 13 : Create an new user and its password
Press 14 : See the user name
Press 15 : See the File System in Detail
Press 16 : See the memory/RAM Space of an system
Press 17 : See the live status of every command output
Press 18 : Read the every file
Press 19 : Run the command output using an file
Press 20 : Print the text/command output message
Press 21 : Speak the text/command output message
Press 22 : See the location of an command
Press 23 : Getting more information of an particular command
Press 24 : See the IP Address of an Network Card
Press 25 : See the Current User Name
Press 26 : Open the calculator
Press 27 : Reboot the system
Press 28 : See the Status of every program
Press 29 : Remove the directory/folder
Press 30 : Exit this Menu\n\n'''))
				if b == 1:
					print("Opening the firefox")
					os.system("firefox &")
				elif b == 2:
					os.system("date")
				elif b == 3:
					os.system("cal")
				elif b == 4:
					month = input("Enter the Month: ")
					year = input("Enter the Year: ")
					os.system("cal {} {}".format(month,year))
				elif b == 5:
					ip = input("Enter the IP Address: ")
					os.system("ping {}".format(ip))
				elif b == 6:
					os.system("jobs")
				elif b == 7:
					os.system("fg")
				elif b == 8:
					folder = input("Enter the folder name: ")
					os.system("mkdir {}".format(folder))
					print("{} Folder Created".format(folder))
				elif b == 9:
					os.system("ls")
				elif b == 10:
					file_name = input("Give the text file name")
					os.system("touch {}.txt".format(file_name))
					print("{}.txt Empty file Created".format(file_name))
				elif b == 11:
					os.system("ls -lh")
				elif b == 12:
					print("Opening the Text Editor....")
					os.system("gedit")
				elif b == 13:
					user_name = input("Give a user_name: ")
					os.system("useradd {}".format(user_name))
					os.system("passwd {}".format(user_name))
				elif b == 14:
					os.system("whoami")
				elif b == 15:
					os.system("df -h")
				elif b == 16:
					os.system("free -m")
				elif b == 17:
					command = input("Give any command: ")
					os.system("watch -n 1 {}".format(command))
				elif b == 18:
					file_name = input("Give the file name: ")
					os.system("cat {}".format(file_name))
				elif b == 19:
					filename = input("Give the file name: ")
					os.system("source {}".format(filename))
				elif b == 20:
					sc = input("What to do want: (string/command) ")
					if sc == "string":
						text = input("Enter a string: ")
						os.system("echo '{}'".format(text))
					else:
						command = input("Enter a command: ")
						os.system("echo `{}`".format(command))
				elif b == 21:
					sc = input("What to do want: (string/command) ")
					if sc == "string":
						text = input("Enter a string: ")
						os.system("espeak-ng '{}'".format(text))
					else:
						command = input("Enter a command: ")
						os.system("espeak-ng `{}`".format(command))
				elif b == 22:
					command = input("Enter a command: ")
					os.system("which {}".format(command))
				elif b == 23:
					command = input("Enter a command name: ")
					os.system("man {}".format(command))
				elif b == 24:
					os.system("ifconfig enp0s3")
				elif b == 25:
					os.system("whoami")
				elif b == 26:
					os.system("bc")
				elif b == 27:
					os.system("reboot")
				elif b == 28:
					os.system("netstat -tnlp")
				elif b == 29:
					ff = input("What to do want: (file/folder) ")
					if ff == "file":
						filename = input("Enter the file name: ")
						os.system("rm -rf {}".format(filename))
					else:
						foldername = input("Enter the folder/location name: ")
						os.system("rmdir {}".format(foldername))
				elif b == 30:
					break
				else:
					print("not supported")
				input("Please Enter to continue the Menu....")

		elif a == "docker":
			while True:
				import os
				os.system("clear")
				os.system("tput setaf 2")
				print("\t\t\tWelcome to the Docker Menu.....\t\t\t")
				os.system("tput setaf 7")
				print("\t\t\t-------------------------------\n\n")
				b = int(input("""Press 1 : See the Version of the docker
Press 2 : List the Images Name of the docker
Press 3 : List all the containers
Press 4 : List the running containers
Press 5 : Download the new images
Press 6 : Search all the images
Press 7 : Start the container with its name or container ID
Press 8 : Stop the container with its name or container ID
Press 9 : Attach the container with its name or container ID
Press 10 : See the information of the Docker
Press 11 : Remove an container or Image
Press 12 : Remove all the containers
Press 13 : Launch the new container
Press 14 : See the Log of an container
Press 15 : Start the docker services
Press 16 : Stop the docker services
Press 17 : Take Help of the Docker
Press 18 : Exit the Docker Menu
\n\n"""))

				if b == 1:
					os.system("docker --version")
				elif b == 2:
					os.system("docker images")
				elif b == 3:
					os.system("docker ps -a")
				elif b == 4:
					os.system("docker ps")
				elif b == 5:
					image = input("Enter the image name: ")
					version = input("Enter the version/tag if need: ")
					os.system("docker pull {}:{}".format(image,version))
				elif b == 6:
					image = input("Enter the image name: ")
					os.system("docker search {}".format(image))
				elif b == 7:
					input_data = input("Enter the container id/name of the container: ")
					os.system("docker start {}".format(input_data))
				elif b == 8:
					input_data = input("Enter the container id/name of the container: ")
					os.system("docker stop {}".format(input_data))
				elif b == 9:
					input_data = input("Enter the container id/name of the container: ")
					os.system("docker attach {}".format(input_data))
				elif b == 10:
					os.system("docker info")
				elif b == 11:
					input_data = input("What do you choose for delete (container/image): ")
					if input_data == "container":
						container = input("Enter the container id/name of the container: ")
						os.system("docker rm -f {}".format(container))
					elif input_data == "image":
						image = input("Enter the image name: ")
						version = input("Enter the version if need: ")
						os.system("docker rmi -f {}:{}".format(image,version))
					else:
						print("not found in search")
				elif b == 12:
					os.system("docker rm -f `docker ps -a -q`")
				elif b == 13:
					image = input("Enter the image name: ")
					version = input("Enter the version if need: ")
					name = input("Enter the name of the container if need: ")
					bash_shell = input("Enter the particular command for use the image if need: ")
					os.system("docker run -it --name {} {}:{} '{}'".format(name,image,version,bash_shell))
				elif b == 14:
					input_data = input("Enter the container id/name of an container: ")
					os.system("docker logs {}".format(input_data))
				elif b == 15:
					os.system("systemctl start docker")
					os.system("systemctl enable docker")
				elif b == 16:
					os.system("systemctl stop docker")
					os.system("systemctll disable docker")
				elif b == 17:
					os.system("docker --help")
				elif b == 18:
					break
				else:
					print("Not Found")

				input("Please Enter to Continue....")
		elif a == "exit":
			print("Thank You for Using our Menu System\n")
			print("Created by Prabhjeet, Pallavi, Sadiya, Saurabh")
			exit()
		elif a == "yum":
			while True:
				import os
				os.system("clear")
				os.system("tput setaf 5")
				print("\t\t\tWelcome to the yum configuration menu....")
				os.system("tput setaf 7")
				print("\t\t\t-----------------------------------------\n\n")
				b = int(input("""
Press 1 : Check the Software Name
Press 2 : Create a yum configuration file
Press 3 : See the yum configuration details
Press 4 : Check the software name
Press 5 : (Install/Uninstall) the software
Press 6 : List the software in yum
Press 7 : Exit the program
\n\n"""))

				if b == 1:
					soft = input("Enter the software name: ")
					os.system("rpm -q {}".format(soft))
				elif b == 2:
					file_name = input("Enter file name: ")
					cd1 = input("Enter your first dvd name: ")
					cd2 = input("Enter your second dvd name: ")
					cd3 = input("Enter you third dvd name: ")
					os.system("touch /etc/yum.repos.d/{}.repo".format(file_name))
					yum_file = open("/etc/yum.repos.d/{}.repo".format(file_name),"w")
					configure_yum = '''[{}]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[{}]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0

[{}]
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable
gpgcheck=0\n'''.format(cd1,cd2,cd3)
					yum_file.write(configure_yum)
					print("Yum has been configured successfully")
				elif b == 3:
					os.system("yum repolist")
				elif b == 4:
					command = input("Enter the command name: ")
					os.system("yum whatprovides {}".format(command))
				elif b == 5:
					yum_iu = input("Choose what do you want (install/uninstall): ")
					if yum_iu == "install":
						soft_name = input("Enter the software name: ")
						os.system("yum install {} -y".format(soft_name))
					elif yum_iu == "uninstall":
						soft_name = input("Enter the software name: ")
						os.system("yum remove {} -y".format(soft_name))
				elif b == 6:
					list_item = input("Enter the software name to check: ")
					os.system("yum list {}".format(list_item))
				elif b == 7:
					break
				else:
					print("It is not exist")
				input("Please Enter to continue...")
		elif a == "aws":
			while True:
				os.system("clear")
				import os
				os.system("tput setaf 5")
				print("\t\t\t\tWelcome to your AWS Menu....")
				os.system("tput setaf 7")
				print("\t\t\t\t----------------------------\n\n")
				b = int(input("""Press 1 for Install the AWS CLI in Linux
Press 2 for check the version of AWS
Press 3 for configure/Login the AWS account
Press 4 for create the Key name
Press 5 for delete the Key name
Press 6 for launch a new instance of an EC2
Press 7 for create a security group
Press 8 for create a new EBS volume
Press 9 for attach a EBS Drive to an instance
Press 10 for start/stop the instance
Press 11 for describe all the instances
Press 12 for describe an particular instance
Press 13 for create a new unique S3 bucket
Press 14 for upload a object/file in an unique bucket
Press 15 for remove the (bucket/object) from S3
Press 16 for create a Cloudfront Distribution
Press 17 for Exit the AWS
\n\n"""))

				if b == 1:
					os.system('curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
					os.system("unzip awscliv2.zip")
					os.system("sudo ./aws/install")
					print("AWS CLI Installed Successfully")
				elif b == 2:
					os.system("aws --version")
				elif b == 3:
					os.system("aws configure")
				elif b == 4:
					key_name = input("Enter your key name: ")
					os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
				elif b == 5:
					key_name = input("Enter your key name: ")
					os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
				elif b == 6:
					ami = input("Enter your image-id: ")
					itype = input("Enter your instance-type: ")
					count = input("How much instances of that image need: ")
					subnet = input("Enter your Subnet-id: ")
					sgid = input("Enter your security group id: ")
					key = input("Enter your key name: ")
					os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}".format(ami,itype,count,subnet,sgid,key))
				elif b == 7:
					sg_name = input("Enter the security group name: ")
					vpc_id = input("Enter the VPC id: ")
					os.system("aws ec2 create-security-group --group-name {} --description 'Team Created' --vpc-id {}".format(sg_name,vpc_id))
				elif b == 8:
					print("Size is limited upto 2GiB not maximum")
					size = input("Enter the size of ebs volume: ")
					region = input("Enter availablity zone: ")
					if int(size) <= 2:
						os.system("aws ec2 create-volume --volume-type gp2 --size {} --availability-zone {}".format(size,region))
					else:
						print("Size should be less than 2GiB")
				elif b == 9:
					volid = input("Enter the volume id: ")
					ec2id = input("Enter the instance id: ")
					os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device '/dev/sdf'".format(volid,ec2id))
				elif b == 10:
					instance = input("Which state of an instance to you want (start/stop): ")
					if instance == "start":
						a = input("Type instance id: ")
						os.system("aws ec2 start-instances --instance-ids {}".format(a))
					elif instance == "stop":
						a = input("Type instance id: ")
						os.system("aws ec2 stop-instances --instance-ids {}".format(a))
					else:
						print("Your different choice is not found...")
				elif b == 11:
					os.system("aws ec2 describe-instances")
				elif b == 12:
					a = input("Type instance id: ")
					os.system("aws ec2 describe-instances --instance-ids {}".format(a))
				elif b == 13:
					bucket = input("Create the Unique Bucket Name: ")
					os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(bucket))
				elif b == 14:
					objectname = input("Enter the object name: ")
					s3name = input("Enter the bucket name: ")
					os.system('aws s3 cp /root/{} s3://{} --acl public-read'.format(objectname,s3name))
				elif b == 15:
					input_name = input("Choose for the deletion (object/bucket): ")
					if input_name == "object":
						object_name = input("Enter the object name: ")
						s3_name = input("Enter the bucket name: ")
						os.system('aws s3 rm s3://{}/{}'.format(s3_name,object_name))
					elif input_name == "bucket":
						bucket = input("Enter the bucket name: ")
						os.system('aws s3api delete-bucket --bucket {} --region ap-south-1'.format(bucket))
					else:
						print("Not Found")
				elif b == 16:
					s3_name = input("Enter your bucket name: ")
					os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(s3_name))
				elif b == 17:
					break
				else:
					print("Not Found other option for AWS")
				input("Please Enter to continue...")
		else:
			print("Not Supported any option....\n")
			input("Press Enter to Continue.....")
