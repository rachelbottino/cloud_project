import boto3
from aws_creator import *

#Cria clients e resource do EC2 e SSM
ec2_client = boto3.client('ec2', region_name='us-east-1')
ec2_resource = boto3.resource('ec2', region_name='us-east-1')

#Key Pair
key_name = ''
key_material = ''
#Ubuntu 18 image id para North Virginia
image_id = 'ami-04b9e92b5572fa0d1'
instance_type = 't2.micro'

#
#Gateway
#
#Security Group
sg_gateway_name = 'gateway_sg'
sg_gateway_description = 'gateway security group'
sg_gateway_id = ''
#Instance
instance_name_gateway = 'gateway'

#
#Load Balancer
#
#Security Group
sg_loadbalancer_name = 'loadbalancer_sg'
sg_loadbalancer_description = 'load balancer nodes security group'
sg_loadbalancer_id = ''
#Instance
instance_name_node1 = 'node1'
instance_name_node2 = 'node2'
instance_name_node3 = 'node3'

#
#Client
#
#Security Group
sg_client_name = 'client_sg'
sg_client_description = 'client security group'
sg_client_id = ''
#Instance
instance_name_client = 'client'

#
#Create security groups
gateway_sg_id = create_security_group(sg_gateway_name,sg_gateway_description)
sg_gateway_file = open("sg_gateway.txt","a")
sg_gateway_file.write(gateway_sg_id)
sg_gateway_file.close()

lb_sg_id = create_security_group(sg_loadbalancer_name,sg_loadbalancer_description)
sg_lbfile = open("sg_loadbalancer.txt","a")
sg_lb_file.write(lb_sg_id)
sg_lb_file.close()

client_sg_id = create_security_group(sg_client_name,sg_client_description)
sg_client_file = open("sg_client.txt","a")
sg_client_file.write(client_sg_id)
sg_client_file.close()

#Create Instances
gateway = create_instance(image_id, instance_type, sg_gateway_name, key_name, instance_name_gateway)
node1 = create_instance(image_id, instance_type, sg_loadbalancer_name, key_name, instance_name_node1)
node2 = create_instance(image_id, instance_type, sg_loadbalancer_name, key_name, instance_name_node2)
node3 = create_instance(image_id, instance_type, sg_loadbalancer_name, key_name, instance_name_node3)
client = create_instance(image_id, instance_type, sg_client_name, key_name, instance_name_client)

id_gateway = gateway[0].id
id_node1 = node1[0].id
id_node2 = node2[0].id
id_node3 = node3[0].id
id_client = client[0].id

gateway = ec2_client.describe_instances(InstanceIds=[id_database])
ip_gateway = gateway['Reservations'][0]['Instances'][0]['PublicIpAddress']
ip_gateway_file = open("ip_gateway.txt","a")
ip_gateway_file.write(ip_gateway)
ip_gateway_file.close()

node1 = ec2_client.describe_instances(InstanceIds=[id_node1])
ip_node1 = node1['Reservations'][0]['Instances'][0]['PublicIpAddress']
ip_node1_file = open("ip_node1.txt","a")
ip_node1_file.write(ip_node1)
ip_node1_file.close() 

node2 = ec2_client.describe_instances(InstanceIds=[id_node2])
ip_node2 = node2['Reservations'][0]['Instances'][0]['PublicIpAddress']
ip_node2_file = open("ip_node2.txt","a")
ip_node2_file.write(ip_node2)
ip_node2_file.close() 

node3 = ec2_client.describe_instances(InstanceIds=[id_node3])
ip_node3 = node3['Reservations'][0]['Instances'][0]['PublicIpAddress']
ip_node3_file = open("ip_node3.txt","a")
ip_node3_file.write(ip_node3)
ip_node3_file.close() 

client = ec2_client.describe_instances(InstanceIds=[id_client])
ip_client = client['Reservations'][0]['Instances'][0]['PublicIpAddress']
ip_client_file = open("ip_client.txt","a")
ip_client_file.write(ip_client)
ip_client_file.close() 