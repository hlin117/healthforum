#!/usr/bin/python
# SQLAlchemy version 0.9.3
from flask import Flask
from datetime import datetime
import simplejson
import json
#import MySQLdb
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import mysql
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, types
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from models import Drugs, SideEffects, SideEffectsDetails

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bbe6adb0b555dc:488c7e4d@us-cdbr-east-05.cleardb.net/heroku_5f9923672d3888a'
app.config['SQLALCHEMY_ECHO'] = True  # only in development!!!
app.config['SQLALCHEMY_PASSWORD'] = '488c7e4d'

#def __init__(self):
my_engine = create_engine('mysql://bbe6adb0b555dc:488c7e4d@us-cdbr-east-05.cleardb.net/heroku_5f9923672d3888a', echo=True, convert_unicode=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=my_engine)
my_session = Session()

#db.create_all(my_engine) # tables are already created

#try:		
#data = simplejson.load(open("drug_sideeffect_retResults.json", "r")) # Maybe use json.loads("drug_sideeffect_retResults.json") ?
#mydata = json.loads("drug_sideeffect_retResults.json")
data = simplejson.load(open("part.json", "r"))

"""
	data =  [{
		"drugName":"some drug",
		"sideEffect":"some side effect",
		"retrievedObjects":
			[{
				"url":"http://www.some.url.om",
				"forumId":"5",
				"title":"some title1",
				"content":"content 1"
			}]
	}]
"""

#druglist=[x['drugName'] for x in data]
with open("test.txt", "a") as myfile:
	druglist=str([x['drugName'] for x in data])
	myfile.write(uniq(druglist))


#print simplejson.dumps(x['drugName'], sort_keys=True, indent=0)

#data = open('part.json', 'r+')
#data = open('drug_sideeffect_retResults.json', 'r+')
#jdata = json.loads(data.read().decode("utf-8"))

#for k,v in jdata:
#	print value

#dr = data['drugName'][0]['side_effects'][0]
#print simplejson.dumps(dr, sort_keys=True, indent=0)

#print data[0]['drugName']

#for i,dr in enumerate(data['drugName']):
#for we in 10000:
#	for dr in data['drugName'][we].itervalues():
#	drug = Drugs(dr)
#	print data[0]
#	print simplejson.dumps(dr, sort_keys=True, indent=0)
#	with open("test.txt", "a") as myfile:
#		myfile.write("appended text")
#	drug = Drugs(dr[i])
#	my_session.add(drug)

#	for se in data['sideEffect']:
#		side_effect = SideEffects(se)
#		my_session.add(side_effect)

#		for j, reO in data['retrievedObjects'][i]:
#			side_effects_details = SideEffectsDetails(reO)
#
#			url = data['retrievedObjects'][j]['url']
#			my_session.add(url)

#			forumid = data['retrievedObjects'][j]['forumId']
#			my_session.add(forumid)
#
#			title = data['retrievedObjects'][j]['title']
#			my_session.add(title)
	
#			content = data['retrievedObjects'][j]['content']
#			my_session.add(content)
#
#except (ValueError, KeyError, TypeError):
#    print "JSON format error"


#process() # run once
#my_session.commit()





