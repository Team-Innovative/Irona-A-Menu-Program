import os
datanode_folder = input("Folder name for datanode: ")
os.system("rm -rf /{}".format(datanode_folder))
os.system("mkdir /{}".format(datanode_folder))
file_hdfs_dn = open("/etc/hadoop/hdfs-site.xml","w")
hdfs_data_dn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>\n'''.format(datanode_folder)
file_hdfs_dn.write(hdfs_data_dn)
