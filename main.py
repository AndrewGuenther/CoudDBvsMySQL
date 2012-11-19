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

#person = PersonBuffer.getNewPerson()
# couchdb.insertPerson(person)

#print mydb.get('dfwf')
#print mydb.executeWrite('DELETE FROM testz')
#print mydb.get('dfwf')
#print mydb.executeWrite("insert into testz set id = %s, value = %s", (1337, 'dsfwef'))
#print mydb.get('dfwf')

for _ in range(1, 1000):
   mydb.insertPerson(PersonBuffer.getNewPerson())

pprint(mydb.getPerson(10))
