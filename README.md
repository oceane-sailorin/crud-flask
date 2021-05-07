## Little flask app with mysql with CRUD functions on Ubuntu 

### Prerequisites python 3.8 installed
install : mysql-server python3-dev libmysqlclient-dev 

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

create config.py
in config.py, add the different configurations

###  add init
create dir app 

create init file : __init__.py (default init file)

in this file: 
    - add the necessary imports
    - initialize a database variable
    - define the app configuration

inside app, create dir static and templates
static is the default directory for static files in Flask (css, js)
templates is the default directory for html  files in Flask

###  add models in sport.py
in this example there is only one simple class for table Wintersport

### add crud functions
create main.py which will be used as the run file

    - import the necessary modules and initialized variables

    - execute the app initialisation 

    - insert routes for each crud function

    - define run conditions

create home.html in templates
    - add html forms for Create, Read, Update and Delete 

### launch  app (default on 5000)
python3 main.py

### result

![app screenshot](app/img/screenshot.png "Title Text")


