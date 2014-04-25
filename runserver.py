#!/usr/bin/python
from flask import Flask
from flask.ext import restful
from flask.ext.restful import reqparse, marshal_with, marshal
from flask.ext.restful.utils import cors
from database import Users, Drugs, SideEffects, URI 
from flask.ext.sqlalchemy import SQLAlchemy

"""
More information about Flask RESTful:
http://flask-restful.readthedocs.org/en/latest/installation.html

More documentation on cors (cross origin resource sharing):
https://github.com/twilio/flask-restful/pull/131

More information on argument passing:
http://flask-restful.readthedocs.org/en/latest/reqparse.html

For the brave souls: To push this server onto heroku,
https://devcenter.heroku.com/articles/getting-started-with-python

"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URI
data = SQLAlchemy(app)

api = restful.Api(app)
api.decorators=[cors.crossdomain(origin='*')]

################################################
################################################

class Drug_info_resource(restful.Resource):
	def get(self, drugname):
		try:
			druginfo = Drugs.query.filter_by(name = drugname).first()
			return {"name": druginfo.name, "concise": druginfo.info}
		except:
			data.session.rollback()
			return "Error...", 500 

api.add_resource(Drug_info_resource, "/drugs/info/<string:drugname>")

# Returns a list of all of the drugs in the database
class Drug_List_resource(restful.Resource):

	def get(self):
		try:
			drugs = Drugs.query.order_by(Drugs.name).all()
			return [{"name": drug.name, "concise": drug.info} for drug in drugs]
		except:
			data.session.rollback()
			return "Error...", 500 

api.add_resource(Drug_List_resource, '/drugs/all')

# Given a drug's name and whether a user is a patient or doctor,
# return a list of side effects corresponding to the user
class Drug_Effect_resource(restful.Resource):

	def get(self, drugName, userType):
		try:
			effectType = "doctor_effect" if userType.lower() == "doctor" else "patient_effect"
			drugId = Drugs.query.filter_by(name = drugName.lower()).first().id

			# TODO: Learn how to do a f***** select statement in SQLAlchemy! There's code to be refractored 
			queryEffects = SideEffects.query.filter_by(drug_id = drugId)
			
			output = dict()
			output["name"] = drugName
			output["userType"] = userType
			output["drugId"] = drugId
			if userType == "doctor":
				output["effects"] = [{"name": query.doctor_effect, "something": "hello"} for query in queryEffects]
			else:
				output["effects"] = [{"name": query.patient_effect, "something": "hello"} for query in queryEffects]
				
			return output
		except:
			data.session.rollback()
			return "Error...", 500 


api.add_resource(Drug_Effect_resource, '/drugs/<string:drugName>/<string:userType>')

# Grabs the drugs that start with the given characters
class Drugs_Substr_resource(restful.Resource):

	def get(self, startChars):
		try:
			drugs = Drugs.query.filter(Drugs.name.startswith(startChars)).all()
			return [drug.name for drug in drugs]
		except:
			data.session.rollback()
			return "Drug not found", 404

api.add_resource(Drugs_Substr_resource, '/drugs/list/<string:startChars>')

# Grabs the drugs and their information that start with the given characters
class Drugs_Substr_Result_resource(restful.Resource):

	def get(self, startChars):
		try:
			drugs = Drugs.query.filter(Drugs.name.startswith(startChars)).all()
			return [{"name": drug.name, "concise": drug.info} for drug in drugs]
		except:
			data.session.rollback() 

api.add_resource(Drugs_Substr_Result_resource, '/drugs/result/<string:startChars>')

################################################
################################################

if __name__ == '__main__':
	app.run(debug=True)