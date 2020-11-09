import os
os.system("tput setaf 8")
print("\t\t\t\tWelcome to the client core-configuration menu.....")
os.system("tput setaf 7")
print("\t\t\t\t--------------------------------------------------")
print("\n\n")
print("""Press 1 : To change the replication factor only
Press 2 : To change the block size(in bytes) only
Press 3 : To change the block size(in bytes) and replication factor both
Press 4 : Not Do Anything remains default as Replication=3 and block size=64MB\n
""")

choice = int(input("Select any one: "))

if(choice == 1):
	rep_size = int(input("Enter The Number of Replication: "))
	hdfs_file_cn = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data_cn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>
</property>
</configuration>/n'''.format(rep_size)
	hdfs_file_cn.write(hdfs_data_cn)
	print("Replication: {} and Block Size: ByDefault(64MB) is configured".format(rep_size))

elif(choice == 2):
	block_size = int(input("Enter the block size in bytes: "))
	hdfs_file_cn = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data_cn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>/n'''.format(block_size)
	hdfs_file_cn.write(hdfs_data_cn)
	print("Replication: ByDefault(3) and Block Size: {} is configured".format(block_size))

elif(choice == 3):
	rep_size = int(input("Enter The Number of Replication: "))
	block_size = int(input("Enter the block size in bytes: "))
	hdfs_file_cn = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data_cn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.replication</name>
<value>{}</value>

<name>dfs.block.size</name>
<value>{}</value>
</property>
</configuration>/n'''.format(rep_size,block_size)
	hdfs_file_cn.write(hdfs_data_cn)
	print("Replication: {} and Block Size: {} is configured".format(rep_size,block_size))

elif(choice == 4):
	hdfs_file_cn = open("/etc/hadoop/hdfs-site.xml","w")
	hdfs_data_cn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>

</configuration>/n'''
	hdfs_file_cn.write(hdfs_data_cn)
	print("Replication: ByDefault(3) and Block Size: ByDefault(64MB) is configured")

else:
	print("Not Found")


