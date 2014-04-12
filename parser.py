#!/usr/bin/python
# SQLAlchemy version 0.9.3
#from healthcode import app
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import mysql
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, types
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.types import TypeDecorator, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from logging import getLogger
import simplejson
import config
import models

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://bbe6adb0b555dc:488c7e4d@us-cdbr-east-05.cleardb.net/heroku_5f9923672d3888a'
app.config['SQLALCHEMY_ECHO'] = True  # only in development!!!
app.config['SQLALCHEMY_PASSWORD'] = '488c7e4d'


class Resources():

	def __init__(self):
		self.engine = None
		self.metadata = None # Collection of tables and their associated schema constructs
		self.session = None

		self.setup_connection()
		
		self.setup_tables() # already done
		self.process() # run once
		self.session.commit()
		app.run()

	def setup_connection(self):
		self.engine = create_engine('mysql://bbe6adb0b555dc:488c7e4d@us-cdbr-east-05.cleardb.net/heroku_5f9923672d3888a', echo=True, convert_unicode=True)
		Session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
		self.session = Session()

	def setup_tables(self):
		db.create_all(self.engine)

	def load_data(self):
		data = simplejson.load(open("drug_sideeffect_retResults.json", "r")) # Maybe use json.loads("drug_sideeffect_retResults.json") ?


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

		for i, dr in enumerate(data['drugName']):
			drug = Drugs(dr)
			self.session.add(drug)

			for se in data['sideEffect']:
				side_effect = SideEffects(se)
				self.session.add(side_effect)

				for j, reO in data['retrievedObjects'][i]:
					side_effects_details = SideEffectsDetails(reO)

					url = data['retrievedObjects'][j]['url']
					self.session.add(url)

					forumid = data['retrievedObjects'][j]['forumId']
					self.session.add(forumid)

					title = data['retrievedObjects'][j]['title']
					self.session.add(title)

					content = data['retrievedObjects'][j]['content']
					self.session.add(content)


