## Little flask app with mysql with CRUD functions on Ubuntu 

### Prerequisites python 3.8 installed
on ubuntu I had to install : mysql-server python3-dev libmysqlclient-dev 

then install with pip :
$ pip3 install Flask sqlalchemy Flask-SQLAlchemy mysql-python 

then configure : sudo mysql_secure_installation and follow instructions

### Database 
$ mysql -u root

### Create user
mysql>CREATE USER 'xxxxx'@'localhost' IDENTIFIED BY 'xxxxxx';

mysql>CREATE DATABASE Sports;

### Grant some privileges (all here because it’s just a dev little app)
mysql>GRANT ALL PRIVILEGES on Sports.* to xxxxx@localhost;

to connect to database : mysql -h localhost -u xxxxx -pxxxxxx Sports

### First step to create a little flask app with some crud functions

instance is the default directory where config variables can be set and that is not pushed to the version control
create directory instance

nano config.py in it

set your SQLALCHEMY_DATABASE_URI and SECRET_KEY as environment variables :
export SECRET_KEY='xxxxxxx'
export SQLALCHEMY_DATABASE_URI='mysql://xxxxx:xxxxxx@localhost/sports'

in config.py, add :
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')

add instance directory in .gitignore


