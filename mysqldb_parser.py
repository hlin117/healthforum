#!/usr/bin/python
import MySQLdb
import csv

db = MySQLdb.connect(host="us-cdbr-east-05.cleardb.net",
                     user="bbe6abd0b555dc",
                     passwd="488c7e4d",
                     db="heroku_5f9923672d3888a")

#with open('druglist.txt','r') as f:
	
cur=db.cursor()
csv_data = csv.reader(file('druglist.csv'))
for dr in csv_data:
	print dr
	try:
		cur.execute('INSERT INTO drugs (drug_name) VALUES(\"%s\")', dr)
	except:
		db.rollback()



#close the connection to the database.
db.commit()
cur.close()
print "Done"







"""
for key in drugs.keys():
        try:
                query = "INSERT INTO drugs (name) VALUES (\"%s\")" % (key)
                cur.execute(query)
                get_drug_id = "SELECT id from drugs WHERE name = \"%s\"" % (key)
                cur.execute(get_drug_id)
                for row in cur.fetchall():
                        drug_id = row[0]
                for side_effect in drugs[key]:
                        val= "INSERT INTO side_effects (id, side_effect) VALUES (\"%d\", \"%s\")" % (drug_id, side_effect)
                        cur.execute(val)
                db.commit()
        except:
                db.rollback()
db.close()


cur = db.cursor() 
cur.execute("SELECT * FROM drugs")


for row in cur.fetchall():
    print "%s %s" % (row[0], row[1])


cur = db.cursor()
cur.execute("SELECT name, side_effect FROM drugs, side_effects WHERE id = drug_id")
for row in cur.fetchall():
    print "%s %s" % (row[0], row[1])

#Parsing the Forum Drug Side Effects
drugs={}
#with open('drugs.txt','r') as f:
#with open('drug_sideeffect_retResults.json','r') as f:
with open('file.txt','r') as f:
	for line in f:
		if "drugName" in line:
			drug_name = line.split(':')[2]
			if drug_name not in drugs.keys():
				drugs[drug_name] = []
		else:
			drugs[drug_name].extend(line.strip().replace('"','').split(' '))

#Storing into Database
cur=db.cursor()
for key in drugs.keys():
	try:
		query = "INSERT INTO drugs (name) VALUES (\"%s\")" % (key)
		cur.execute(query)
		get_drug_id = "SELECT id from drugs WHERE name = \"%s\"" % (key)
		cur.execute(get_drug_id)
		for row in cur.fetchall():
			drug_id = row[0]
		for side_effect in drugs[key]:
			val= "INSERT INTO side_effects (id, side_effect) VALUES (\"%d\", \"%s\")" % (drug_id, side_effect)
			cur.execute(val)
		db.commit()
	except:
		db.rollback()
db.close()

"""
