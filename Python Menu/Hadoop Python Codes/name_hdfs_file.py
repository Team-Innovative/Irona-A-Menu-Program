import os
namenode_folder = input("Folder name for namenode: ")
os.system("rm -rf /{}".format(namenode_folder))
os.system("mkdir /{}".format(namenode_folder))
file_hdfs_nn = open("/etc/hadoop/hdfs-site.xml","w")
hdfs_name_nn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>\n'''.format(namenode_folder)
file_hdfs_nn.write(hdfs_name_nn)
