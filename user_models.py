from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import fields, marshal

#db = SQLAlchemy(Flask(__name__))
def init_users(db):

# NOTE: Shows up in database as users, NOT Users
# TODO: We need more tables! Need a table for doctors as well as patients.
	class Users(db.Model):
		id = db.Column(db.Integer, primary_key=True)
		first_name = db.Column(db.String(30))
		last_name = db.Column(db.String(30))
		email = db.Column(db.String(50))
		isDoctor = db.Column(db.Boolean)


		def __init__(self, first, last, dob):
			self.first_name = first
			self.last_name = last
			self.dob = dob

		# Marshalling documentation:
		# http://flask-restful.readthedocs.org/en/latest/api.html
		# http://flask-restful.readthedocs.org/en/latest/fields.html
		@staticmethod
		def fields():
			users_fields = {
				'first_name': fields.String,
				'last_name': fields.String,
				'isDoctor': fields.Boolean,
				'email': fields.email
			}
			return users_fields
		
	class Patients(db.Model):
		id = db.Column(db.Integer, primary_key = True)
		user_id = db.Column(db.Integer)
		dob = db.Column(db.Date)
		weight_lbs = db.Column(db.SMALLINT)
		height_in = db.Column(db.SMALLINT)
		gender = db.Column(db.Enum('F', 'M'))

		def __init__(self, dob, weight, height_ft, height_in, gender):
			if height_in >= 12:
				print "WARNING: height_in >= 12"
			self.dob = dob
			self.weight_lbs = weight
			self.height_in = height_ft * 12 + height_in
			self.gender = gender

		@staticmethod
		def fields():
			patient_fields = {
				'dob': fields.DateTime,
				'height_ft': fields.Integer,
				'height_in': fields.Integer,
				'gender': fields.String 
			}
			return patient_fields

	class Doctors(db.Model):
		id = db.Column(db.Integer, primary_key = True)
		user_id = db.Column(db.Integer)
		hospital = db.Column(db.String(100))
		specialization = db.Column(db.String(60))
		title = db.Column(db.String(52))

		def __init__(self, user_id, hospital, specialization, title):
			self.user_id = user_id
			self.hospital = hospital
			self.specialization = specialization
			self.title = title

		# TODO: Create a fields methor
