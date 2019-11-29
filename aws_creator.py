import boto3

def key_pair_exists(key_name,ec2_client):
	response_keys = ec2_client.describe_key_pairs()
	keys = response_keys['KeyPairs']
	exist_key = []
	for key in keys:
		exist_key.append(key['KeyName'])
	if key_name in exist_key:
		dlt_key = ec2_client.delete_key_pair(KeyName=key_name)
		print("Key deleted")

def import_key_pair(key_name,key_material,ec2_client):
	key_pair_exists(key_name,ec2_client)
	key_pair = ec2_client.import_key_pair(KeyName=key_name,PublicKeyMaterial=(key_material))
	print("Key Pair Imported")

def create_key_pair(key_name,ec2_client):	
	key_pair_exists(key_name)
	key_pair = ec2_client.create_key_pair(KeyName=key_name)
	keyval = key_pair['KeyMaterial']
	outfile = open(key_pem,'w')
	outfile.write(keyval)
	outfile.close()
	print('Key Pair created successfully')

def create_security_group(sg_name,sg_description, ec2_client):
	response_sg = ec2_client.describe_security_groups()
	security_groups = response_sg['SecurityGroups']
	exist_sg = []
	for group in security_groups:
		exist_sg.append(group['GroupName'])
	if sg_name in exist_sg:
		dlt_sg = ec2_client.delete_security_group(GroupName=sg_name)
		print("Security Group deleted")
	security_group = ec2_client.create_security_group(GroupName=sg_name, Description=sg_description)
	my_group = (ec2_client.describe_security_groups(GroupNames=[sg_name])['SecurityGroups'])
	sg_group_id = my_group[0]['GroupId']
	return(sg_group_id)

def create_instance(image_id, instance_type, sg_name, key_name, instance_name ,ec2_resource):
	instancia = ec2_resource.create_instances(ImageId=image_id,
         InstanceType=instance_type,
         MinCount=1, MaxCount=1,
         SecurityGroups=[sg_name],
         KeyName=key_name,
         TagSpecifications=[{'ResourceType': 'instance', 'Tags': [{'Key': 'Name','Value': instance_name}]}]
         )
	return instancia