import boto3
from aws_creator import *

#Cria client e resource do EC2
ec2_client = boto3.client('ec2')

#Security Groups IDs
id_sg_db_file = open("sg_db.txt","r")
id_sg_db= id_sg_db_file.readlines()[0]

id_ws_lb_file = open("sg_ws.txt","r")
id_ws_lb = id_ws_lb_file.readlines()[0]

#Instance IPS
ip_gateway_file = open("ip_gateway.txt","r")
ip_gateway = ip_gateway_file.readlines()[0]+"/20"

ip_server_file = open("ip_ws.txt","r")
ip_server = ip_server_file.readlines()[0]+"/20"

ip_db_file = open("ip_db.txt","r")
ip_db = ip_db_file.readlines()[0]+"/20"


#
# Security Groups Inbounds
#
ec2_client.authorize_security_group_ingress(GroupId=id_sg_db, IpPermissions=[{'FromPort': '-1', 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': ip_server'/20', 'Description':'server'}]},{"FromPort": 22,"IpProtocol": "tcp","IpRanges": [{"CidrIp": "0.0.0.0/0","Description": "ssh"}],"Ipv6Ranges": [{"CidrIpv6": "::/0","Description": "ssh"}],"ToPort": 22}])
ec2_client.authorize_security_group_ingress(GroupId=id_sg_ws, IpPermissions=[{'FromPort': '-1', 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': ip_gateway'/20', 'Description':'gateway'},{'CidrIp': ip_db'/20', 'Description':'database'}]},{"FromPort": 22,"IpProtocol": "tcp","IpRanges": [{"CidrIp": "0.0.0.0/0","Description": "ssh"}],"Ipv6Ranges": [{"CidrIpv6": "::/0","Description": "ssh"}],"ToPort": 22}])