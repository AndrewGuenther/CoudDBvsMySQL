from util.personbuffer import PersonBuffer
from db.mysqldb import MySqlDb
from db.couchdb import CouchDB

mydb = MySqlDb()
couchdb = CouchDB()

#person = PersonBuffer.getNewPerson()
# couchdb.insertPerson(person)

#print mydb.get('dfwf')
#print mydb.executeWrite('DELETE FROM testz')
#print mydb.get('dfwf')
#print mydb.executeWrite("insert into testz set id = %s, value = %s", (1337, 'dsfwef'))
#print mydb.get('dfwf')

for _ in range(1, 50):
   mydb.insertPerson(PersonBuffer.getNewPerson())
