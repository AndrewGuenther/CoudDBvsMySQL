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

for _ in range(1, 10):
   person = PersonBuffer.getNewPerson()
   mydb.insertPerson(person)
   couchdb.insertPerson(person)


pprint(mydb.getPerson(10))
print "--------"
pprint(couchdb.getPerson(10))
