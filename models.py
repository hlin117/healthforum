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

app = Flask(__name__)
db = SQLAlchemy(app)

'''
create table if not exists users (user_id int not null auto_increment, primary key (user_id), first_name varchar(30), last_name varchar(30), birthdate date, age int(3), weight_lbs int(3), height_inches int(4), gender char(1)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''

class Users(db.Model):
	__tablename__ = "users"
	user_id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30))
	last_name = db.Column(db.String(30))
	dob = db.Column(db.DateTime)
	weight_lbs = db.Column(db.Integer)
	height_inches = db.Column(db.Integer)
	gender = db.Column(db.String(1))

	def __init__(self, resource):
		self.first_name = resource['first_name']
		self.last_name = resource['last_name']
		self.dob = resource['dob']
		self.weight_lbs = resource['weight_lbs']
		self.height_inches = resource['height_inches']
		self.gender = resource['gender']

	def __repr__(self):
		return '<User %s %s>' % (self.first_name, self.last_name)

'''
create table if not exists drugs (drug_id int not null auto_increment, primary key (drug_id), drug_name varchar(50), drug_description mediumtext ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''

class Drugs(db.Model):
	__tablename__ = "drugs"
	drug_id = db.Column(db.Integer, primary_key=True)
	drug_name = db.Column(db.String(50), unique=True)
	# Probably want a drug description here later

	def __init__(self, resource):
		self.drug_name = resource['drugName']

	def __repr__(self):
		return '<Drug %s>' % self.drug_name

'''
create table if not exists side_effects (side_effect_id int not null auto_increment, primary key (side_effect_id), drug_id int, foreign key (drug_id) references drugs(drug_id) on update cascade on delete cascade, side_effect varchar(150)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''

class SideEffects(db.Model):
	__tablename__ = "side_effects"
	side_effects_id = db.Column(db.Integer, primary_key=True)
	side_effect = db.Column(db.String(150))

	drug_id = db.Column(db.Integer, db.ForeignKey('drug.drug_id'))
	drug = db.relationship('Drugs', backref=db.backref('posts', lazy='dynamic'))

	def __init__(self, resource):
		self.side_effect = resource['sideEffect']

	def __repr__(self):
		return '<Side Effect %r>' % self.side_effect

'''
create table if not exists side_effects_details (side_effect_details_id int not null auto_increment, primary key (side_effect_details_id), side_effects_id int, foreign key (side_effects_id) references side_effects(side_effect_id) on update cascade on delete cascade, url varchar(250), forum_id varchar(30), title varchar(100), content mediumtext ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''

class SideEffectsDetails(db.Model):
	__tablename__ = "side_effects_details"
	side_effects_details_id = db.Column(db.Integer, primary_key=True)
	side_effect = db.Column(db.String(150))
	url = db.Column(db.String(250), unique=True)
	title = db.Column(db.String(100))
	forum_id = db.Column(db.String(30), unique=True)
	content = db.Column(db.Text)

	side_effects_id = db.Column(db.Integer, db.ForeignKey('side_effects.side_effects_id'))
	side_effects = db.relationship('SideEffects', backref=db.backref('posts', lazy='dynamic'))

	def __init__(self, resource):
		self.url = resource['url']
		self.title = resource[' title']
		self.forum_id = resource['forumId']
		self.content = resource['content']

	def __repr__(self):
		return '<Side Effect Details %s>' % self.title

