import os
namenode_IP = input("Provide namenode IP: ")
namenode_port = input("Provide Port Number at which you want to run namenode service: ")
file_core_nn = open("/etc/hadoop/core-site.xml","w")
core_name_nn = '''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!--Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:{}</value>
</property>
</configuration>\n'''.format(namenode_IP,namenode_port)
file_core_nn.write(core_name_nn)
