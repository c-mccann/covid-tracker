Covid Tracker
============

Requirements
------------
* Create a basic Django application.
* Consume the data from the disease.sh API to populate the database (of your
choice) with data from all countries. A one time setup is suitable.
* Allow for querying of the database through a REST API for the countries listed
below. The user should be able to select a country from a list of countries.
* Show the data for the selected country on a web page. Minimum data that should
be displayed is:
  * Name of the country
  * Total cases
  * Total deaths
  * Total recovered
  * Allow the user to update the data.
  * Document your local setup instructions.

<br />

* Use the following countries and their codes:
  * Ireland: ie
  * Germany: de
  * Italy: it
  * UK:gb
  * Spain: es

<br />

* sample data can be found here:
  * https://disease.sh/v3/covid-19/countries


Setup
-----
Computer:
* Macbook Pro (16-inch, 2021)
* Chip    Apple M1 Pro
* Memory  16GB
  * python version: 3.10.6
  * npm version: 8.7.0

DB:
* PostgreSQL - Raspberry Pi 4 8Gb
  * postgres (PostgreSQL) 11.16 (Raspbian 11.16-0+deb10u1)
  
Environment
-----------
Backend\
available at localhost:8000:

* created environment using: python3 -m venv env
* activated it using source env/bin/activate
* when env activated, ran server using: python manage.py runserver
* to create database tables run:
  * python manage.py makemigrations
  * python manage.py migrate
  * please run script in res/scripts/add-countries.sql to add selectable countries
  
<br />

* installations within env:
  * python -m pip install django
  * python -m pip install psycopg2-binary
  * python -m pip install django-debug-toolbar
  * python -m pip install requests
  * python -m pip install djangorestframework
  * python -m pip install django-cors-headers

Frontend\
available at localhost:8080:

* in root project folder, created 'client' folder
* created client using: vue create disease_client
* within client/disease_client dir:
  * npm install axios
  * npm install @coreui/coreui
* ran using: npm run serve


API
---
endpoints:
* api/v1/data
  * gets all covid data stored in db
* api/v1/data/\<str:iso_code\>
  * gets a country's covid data by iso code
* api/v1/country
  * get's all countries stored in disease_country table, the 5 requested countries are stored here 
* api/fn/data
  * gets all covid data stored in db, uses a function rather than a class to do this.
* api/fn/data/\<str:iso_code\> 
  * gets a country's covid data by iso code, uses a function rather than a class to do this.

Configuration
-------------
app/secret_config.py contains 6 variables, change to suit your settings:
> db_engine = 'django.db.backends.postgresql'\
> db_name = 'disease'\
> db_user =  ''\
> db_password = ''\
> db_host = ''\
> db_port = '5432'
