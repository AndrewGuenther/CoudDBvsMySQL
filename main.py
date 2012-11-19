from pprint import pprint
from util.personbuffer import PersonBuffer
from db.mysqldb import MySqlDb
from db.couchdb import CouchDB

mydb = MySqlDb()
couchdb = CouchDB()

# Drop all tables and start from scratch.
schema = open('schema.sql').read()
schemaStatements = schema.split(';\n')
for statement in schemaStatements:
   if statement:
      mydb.executeWrite(statement)

for _ in range(1, 100):
   person = PersonBuffer.getNewPerson()

   if person['femaleParent']:
      child = person

   mydb.insertPerson(person)
   couchdb.insertPerson(person)

personid = child['id']

pprint(mydb.getPersonAndParents(personid))
print "--------"
pprint(couchdb.getPersonAndParents(personid))


# print "---- Update ----"

# person = mydb.getPerson(personid)
# person[0]['age'] = 1234
# person[0]['id'] = personid
# mydb.updatePerson(person[0])

# person = couchdb.getPerson(personid)
# print person
# person['age'] = 1234
# couchdb.updatePerson(person)

# pprint(mydb.getPerson(personid))
# print "--------"
# pprint(couchdb.getPerson(personid))
