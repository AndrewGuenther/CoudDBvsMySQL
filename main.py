from db.mysqldb import MySqlDb
from db.couchdb import CouchDB

mydb = MySqlDb()
couchdb = CouchDB()

print couchdb.get('john')
print mydb.get('dfsdf')
