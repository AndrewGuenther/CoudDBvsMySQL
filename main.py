from db.mysqldb import MySqlDb
from db.couchdb import CouchDB

mydb = MySqlDb()
couchdb = CouchDB()

keys = ['one', 'two', 'three', 'four', 'five',
      'six', 'seven', 'eight', 'nine', 'ten']

for i in range(0, 10000):
   key = keys[i % len(keys)]
   couchdb.get(key)
   mydb.get(key)
