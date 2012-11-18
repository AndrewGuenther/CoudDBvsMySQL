from mysqldb import MySqlDb
from couchdb import CouchDB

mydb = MySqlDb()
couchdb = CouchDB()

print couchdb.get('john')
