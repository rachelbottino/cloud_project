import boto3
from aws_creator import *

#Cria client e resource do EC2
ec2_client = boto3.client('ec2')

#Security Groups IDs
id_sg_gateway_file = open("sg_gateway.txt","r")
id_sg_gateway = id_sg_gateway_file.readlines()[0]

id_sg_lb_file = open("sg_loadbalancer.txt","r")
id_sg_lb = id_sg_lb_file.readlines()[0]

id_sg_client_file = open("sg_client.txt","r")
id_sg_client = id_sg_client_file.readlines()[0]

#Instance IPS
ip_gateway_file = open("ip_gateway.txt","r")
ip_gateway = ip_gateway_file.readlines()[0]+"/20"

ip_node1_file = open("ip_node1.txt","r")
ip_node1 = ip_node1_file.readlines()[0]+"/20"

ip_node2_file = open("ip_node2.txt","r")
ip_node2 = ip_node2_file.readlines()[0]+"/20"

ip_node3_file = open("ip_node3.txt","r")
ip_node3 = ip_node3_file.readlines()[0]+"/20"

ip_client_file = open("ip_client.txt","r")
ip_client = ip_client_file.readlines()[0]"/20"

ip_server_file = open("ip_webserver.txt","r")
ip_server = ip_gateway_file.readlines()[0]+"/20"

#
# Security Groups Inbounds
#
#
ec2_client.authorize_security_group_ingress(GroupId=id_sg_gateway, IpPermissions=[{'FromPort': '-1', 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': ip_server'/20', 'Description':'server'},{'CidrIp': ip_node1'/20', 'Description':'node1'},{'CidrIp': ip_node2'/20', 'Description':'node2'},{'CidrIp': ip_node3'/20', 'Description':'node3'}]},{"FromPort": 22,"IpProtocol": "tcp","IpRanges": [{"CidrIp": "0.0.0.0/0","Description": "ssh"}],"Ipv6Ranges": [{"CidrIpv6": "::/0","Description": "ssh"}],"ToPort": 22}])
ec2_client.authorize_security_group_ingress(GroupId=id_sg_lb, IpPermissions=[{'FromPort': '-1', 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': ip_gateway'/20', 'Description':'gateway'},{'CidrIp': ip_client'/20', 'Description':'client'}]},{"FromPort": 22,"IpProtocol": "tcp","IpRanges": [{"CidrIp": "0.0.0.0/0","Description": "ssh"}],"Ipv6Ranges": [{"CidrIpv6": "::/0","Description": "ssh"}],"ToPort": 22}])
ec2_client.authorize_security_group_ingress(GroupId=id_sg_client, IpPermissions=[{'FromPort': '-1', 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': ip_node1'/20', 'Description':'node1'},{'CidrIp': ip_node2'/20', 'Description':'node2'},{'CidrIp': ip_node3'/20', 'Description':'node3'}]},{"FromPort": 22,"IpProtocol": "tcp","IpRanges": [{"CidrIp": "0.0.0.0/0","Description": "ssh"}],"Ipv6Ranges": [{"CidrIpv6": "::/0","Description": "ssh"}],"ToPort": 22}])
