import boto3
import time
from aws_creator import *

#Create EC2 client and resource
#North-California (us-west-1)
ec2_client_west = boto3.client('ec2', region_name='us-west-1')
ec2_resource_west = boto3.resource('ec2', region_name='us-west-1')
#North-Virginia (us-east-1)
ec2_client_east = boto3.client('ec2', region_name='us-east-1')
ec2_resource_east = boto3.resource('ec2', region_name='us-east-1')
el_client = boto3.client('elb', region_name='us-east-1')

#Insert your key pair's informations
key_name = ''
key_material = ''
#Ubuntu 18 image id - North-California
west_image_id = 'ami-0dd655843c87b6930'
#Ubuntu 18 image id - North-Virginia
east_image_id = 'ami-04b9e92b5572fa0d1'
#Instance
instance_type = 't2.micro'

#
#Database
#Security Group
sg_database_name = 'proj_sg_db'
sg_database_description = 'Database security group'
sg_group_id = ''
#Instance
instance_database_name = 'p_database'
#
#Webserver
#Security Group
sg_webserver_name = 'proj_sg_ws'
sg_webserver_description = 'Webserver security group'
sg_group_id = ''
#Instance
instance_webserver_name = 'p_webserver'
#
#Gateway
#Security Group
sg_gateway_name = 'proj_gateway_sg'
sg_gateway_description = 'gateway security group'
sg_gateway_id = ''
#Instance
instance_name_gateway = 'p_gateway'
#
#Load Balancer
load_balancer_name = 'ploadbalancer'
#Security Group
sg_loadbalancer_name = 'proj_loadbalancer_sg'
sg_loadbalancer_description = 'load balancer nodes security group'
sg_loadbalancer_id = ''
#Instance
instance_name_node1 = 'p_node1'
instance_name_node2 = 'p_node2'
instance_name_node3 = 'p_node3'
#
#Client
#Security Group
sg_client_name = 'proj_client_sg'
sg_client_description = 'client security group'
sg_client_id = ''
#Instance
instance_name_client = 'p_client'

#################################################
#Importing your key pair
#################################################
import_key_pair(key_name,key_material,ec2_client_east)

#################################################
#Create security groups
#################################################
print("Creating security groups...")
#North California
database_sg_id = create_security_group(sg_database_name, sg_database_description, ec2_client_west)
webserver_sg_id = create_security_group(sg_webserver_name, sg_webserver_description, ec2_client_west)
#North Virginia
gateway_sg_id = create_security_group(sg_gateway_name, sg_gateway_description, ec2_client_east)
lb_sg_id = create_security_group(sg_loadbalancer_name, sg_loadbalancer_description, ec2_client_east)
client_sg_id = create_security_group(sg_client_name, sg_client_description, ec2_client_east)

print(lb_sg_id)

#################################################
#Create Instances
#################################################
print("Creating Instances...")
#North California
database = create_instance(west_image_id, instance_type, sg_database_name, key_name, instance_database_name, ec2_resource_west)
webserver = create_instance(west_image_id, instance_type, sg_webserver_name, key_name, instance_webserver_name, ec2_resource_west)
#North Virginia
gateway = create_instance(east_image_id, instance_type, sg_gateway_name, key_name, instance_name_gateway, ec2_resource_east)
node1 = create_instance(east_image_id, instance_type, sg_loadbalancer_name, key_name, instance_name_node1, ec2_resource_east)
node2 = create_instance(east_image_id, instance_type, sg_loadbalancer_name, key_name, instance_name_node2, ec2_resource_east)
node3 = create_instance(east_image_id, instance_type, sg_loadbalancer_name, key_name, instance_name_node3, ec2_resource_east)
client = create_instance(east_image_id, instance_type, sg_client_name, key_name, instance_name_client, ec2_resource_east)

time.sleep(30)
#Instances IP Address
ip_db = ec2_client_west.describe_instances(InstanceIds=[database[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip database: ", ip_db)
ip_ws = ec2_client_west.describe_instances(InstanceIds=[webserver[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip webserver: ", ip_ws)
ip_gateway = ec2_client_east.describe_instances(InstanceIds=[gateway[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip gateway: ", ip_gateway)
ip_node1 = ec2_client_east.describe_instances(InstanceIds=[node1[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip node1: ", ip_node1)
ip_node2 = ec2_client_east.describe_instances(InstanceIds=[node2[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip node2: ", ip_node2)
ip_node3 = ec2_client_east.describe_instances(InstanceIds=[node3[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip node3: ", ip_node3)
ip_client = ec2_client_east.describe_instances(InstanceIds=[client[0].id])['Reservations'][0]['Instances'][0]['PublicIpAddress']
print("ip client: ", ip_client)

##################################################
# Security Groups Inbounds
##################################################
print("Authorizing security groups ingrees...")
#North California
ec2_client_west.authorize_security_group_ingress(GroupId=database_sg_id, IpPermissions=[{'IpProtocol': '-1', 'IpRanges': [{'CidrIp': ip_ws+'/20'}]},{'FromPort': 22,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 22}])
ec2_client_west.authorize_security_group_ingress(GroupId=webserver_sg_id, IpPermissions=[{'IpProtocol': '-1', 'IpRanges': [{'CidrIp': ip_gateway+'/20'},{'CidrIp': ip_db+'/20'}]},{'FromPort': 22,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 22}])
#North Virginia
ec2_client_east.authorize_security_group_ingress(GroupId=gateway_sg_id, IpPermissions=[{'IpProtocol': '-1', 'IpRanges': [{'CidrIp': ip_ws+'/20'},{'CidrIp': ip_node1+'/20'},{'CidrIp': ip_node2+'/20'},{'CidrIp': ip_node3+'/20'}], 'ToPort': -1},{'FromPort': 22,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 22}])
ec2_client_east.authorize_security_group_ingress(GroupId=lb_sg_id, IpPermissions= [{'FromPort': 80, 'IpProtocol': 'tcp' ,'IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 80},{'IpProtocol': '-1','IpRanges': [{'CidrIp': ip_gateway+'/20'},{'CidrIp': ip_client+'/20'}]},{'FromPort': 22,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 22},{'FromPort': 5000,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 5000}])
ec2_client_east.authorize_security_group_ingress(GroupId=client_sg_id, IpPermissions= [{'IpProtocol': '-1', 'IpRanges': [{'CidrIp': ip_node1+'/20'},{'CidrIp': ip_node2+'/20'},{'CidrIp': ip_node3+'/20'}]},{'FromPort': 22,'IpProtocol': 'tcp','IpRanges': [{'CidrIp': '0.0.0.0/0'}],'Ipv6Ranges': [{'CidrIpv6': '::/0'}],'ToPort': 22}])

##################################################
# Load Balancer
##################################################
print("Creating load balancer...")
load_balancer = el_client.create_load_balancer(
	LoadBalancerName=load_balancer_name,
	Listeners=[
        {'Protocol': 'HTTP','LoadBalancerPort': 80,'InstanceProtocol': 'HTTP','InstancePort': 80},
        {'Protocol': 'HTTP','LoadBalancerPort': 5000,'InstanceProtocol': 'HTTP','InstancePort': 5000}
    ],
    AvailabilityZones=[
    	'us-east-1a',
    	'us-east-1b',
    	'us-east-1c',
    	'us-east-1d',
    	'us-east-1e',
    	'us-east-1f'
    ],
    SecurityGroups=[
        lb_sg_id
    ],
    Scheme='internet-facing'
)

el_client.register_instances_with_load_balancer(
    LoadBalancerName=load_balancer_name,
    Instances=[
    	{
	        'InstanceId': node1[0].id
        },
        {
            'InstanceId': node2[0].id
        },
        {
            'InstanceId': node3[0].id
        }
    ]
)

print("Load Balancer: ", load_balancer)

el.client.configure_health_check(
    LoadBalancerName=load_balancer_name,
    HealthCheck={
        'Target': 'TCP:5000',
        'Interval': 5,
        'Timeout': 30,
        'UnhealthyThreshold': 2,
        'HealthyThreshold': 10
    }
)
