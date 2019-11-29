***
# Local Machine
Install Boto 3 via pip:<br>
`pip install boto3`

Install AWS Client via pip:<br>
`pip install awscli`

Configure your credentials:<br>
`aws configure`

Clone Cloud Project repository:<br>
`git clone git clone https://github.com/rachelbottino/cloud_project.git`<br>
`cd cloud_repository`<br>

Insert your Key Pair information:<br>
`nano project_create.py`<br>
![](https://github.com/rachelbottino/cloud_project/blob/master/images/keypair.PNG)<br>

Run project_create.py:<br>
`python project_create.by`

SSH connect to all created instances
***
# Database Instance
Clone Cloud Project repository:<br>
`git clone git clone https://github.com/rachelbottino/cloud_project.git`<br>
`cd cloud_project`<br>
`sh database.sh`<br>
`sudo mysql -u root`<br>
`GRANT ALL ON projeto.* TO user_db@<'ip_server'> IDENTIFIED BY 'cloud';`<br>
`exit`<br>

Edit mysql.cnf file, commenting 'bind-address = 127.0.0.1':<br>
`sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf`<br>
![](https://github.com/rachelbottino/cloud_project/blob/master/images/mysql_file.PNG)<br>
`sudo service mysql restart`<br>
***
# Server Instance
Clone Cloud Project repository:<br>
`git clone https://github.com/rachelbottino/cloud_project.git`<br>
`cd cloud_project`<br>
`sh server.sh`<br>
Edit server.py file, inserting database's IP address in "host":<br>
`nano server.py`<br>
![](https://github.com/rachelbottino/cloud_project/blob/master/images/mysql_host.PNG)<br>
`python3 server.py`<br>
***
# Gateway Instance
Clone Cloud Project repository:<br>
`git clone https://github.com/rachelbottino/cloud_project.git`<br>
`cd cloud_project`<br>
`sh nodes.sh`<br>
Edit route.py file, inserting webserver's IP address:<br>
`nano route.py`<br>
![](https://github.com/rachelbottino/cloud_project/blob/master/images/server.PNG)<br>
`python3 route.py`
***
# Node Instances
Clone Cloud Project repository:<br>
`git clone https://github.com/rachelbottino/cloud_project.git`<br>
`cd cloud_project`<br>
`sh nodes.sh`<br>
Edit route.py file, inserting gateway's IP address:<br>
`nano route.py`<br>
![](https://github.com/rachelbottino/cloud_project/blob/master/images/server.PNG)<br>
`python3 route.py`
***
# Client Instance
Clone Cloud Project repository:<br>
`git clone https://github.com/rachelbottino/cloud_project.git`<br>
`cd cloud_project`<br>
`sh client.sh`<br>
Edit client file, inserting DNS Name:<br>
`nano client`<br>
![](https://github.com/rachelbottino/cloud_project/blob/master/images/client_c.PNG)<br>
`chmod +x client`
Wait a few minutes<br>
Test a request:<br>
`./client listar`
