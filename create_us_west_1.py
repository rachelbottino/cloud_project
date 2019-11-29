import boto3
from aws_creator import *

#Cria client e resource do EC2
ec2_client = boto3.client('ec2', region_name='us-west-1')
ec2_resource = boto3.resource('ec2', region_name='us-west-1')

#Variáveis da Key Pair
key_name = ''
key_material = ''

#Ubuntu 18 image id para North-California
image_id = 'ami-0dd655843c87b6930'
instance_type = 't2.micro'
#
#Database
#
#Security Group
sg_database_name = 'sg_db'
sg_database_description = 'Database security group'
sg_group_id = ''
#Instance
instance_database_name = 'database'

#
#Webserver
#
#Security Group
sg_webserver_name = 'sg_ws'
sg_webserver_description = 'Webserver security group'
sg_group_id = ''
#Instance
instance_webserver_name = 'webserver'


#Importing your key pair
import_key_pair(key_name,key_material)

#Create security groups
database_sg_id = create_security_group(sg_database_name,sg_database_description)
sg_db_file = open("sg_db.txt","a")
sg_db_file.write(database_sg_id)
sg_db_file.close()

webserver_sg_id = create_security_group(sg_webserver_name,sg_webserver_description)
sg_ws_file = open("sg_ws.txt","a")
sg_ws_file.write(webserver_sg_id)
sg_ws_file.close()

#Create Instances
database = create_instance(image_id, instance_type, sg_database_name, key_name, instance_database_name)
webserver = create_instance(image_id, instance_type, sg_webserver_name, key_name, instance_webserver_name)

id_database = database[0].id
id_webserver = webserver[0].id
print("Id database: "+id_database,"Id Webserver: "+id_webserver)

db = ec2_client.describe_instances(InstanceIds=[id_database])
ip_db = db['Reservations'][0]['Instances'][0]['PublicIpAddress']
ip_db_file = open("ip_db.txt","a")
ip_db_file.write(ip_db)
ip_db_file.close() 

ws = ec2_client.describe_instances(InstanceIds=[id_webserver])
ip_ws = ws['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("Ip database: "+ip_db, "Ip webserver: "+ip_ws)
ip_ws_file = open("ip_webserver.txt","a")
ip_ws_file.write(ip_ws)
ip_ws_file.close() 

