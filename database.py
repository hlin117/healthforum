from flask import Flask 
from drug_models import init_drugs
from user_models import init_users
from flask.ext.sqlalchemy import SQLAlchemy

useHenry = False

# URLS for the databases. The default one is henryURI
# the clearDB database has been deleted! I commented out herokuURI for this reason.
henryURI = 'mysql://halin2_guest:helloworld@engr-cpanel-mysql.engr.illinois.edu/halin2_sample'
testURI = 'mysql://halin2_guest:helloworld@engr-cpanel-mysql.engr.illinois.edu/halin2_test'

URI = henryURI if useHenry else testURI

# In runserver.py, the code will not be able to access these global vars 
databaseApp = Flask(__name__)
databaseApp.config['SQLALCHEMY_DATABASE_URI'] = URI
db = SQLAlchemy(databaseApp)

# TODO: Initialize drug models
# TODO: Initialize user models
init_drugs(db)
init_users(db)
