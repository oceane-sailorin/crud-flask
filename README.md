##Little flask app with mysql

###Prerequisites python 3.8 mysql installed 
$ pip install flask sqlalchemy flask-sqlalchemy

on ubuntu I had to install : sudo apt-get install python3-dev libmysqlclient-dev 

before : 

$ pip install mysqlclient

###Database 
$ mysql -u root

###Create user
mysql>CREATE USER 'xxxxx'@'localhost' IDENTIFIED BY 'xxxxxx';

mysql>CREATE DATABASE sports;

###Grant some privileges (all here because it’s just a dev little app)
mysql>GRANT ALL PRIVILEGES on sports.* to xxxxx@localhost;

###First step to create a little flask app with some crud functions




