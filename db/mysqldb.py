from pprint import pprint

from db import DB
import MySQLdb

class MySqlDb(DB):
   def __init__(self):
      self.master = self.connect("ip-10-168-7-254.us-west-1.compute.internal")

      self.reads = []
      self.reads.append(self.master)
      self.reads.append(self.connect("ip-10-160-183-128.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-160-90-29.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-168-111-37.us-west-1.compute.internal"))

      # Used for round robin reads.
      self.currentReadDb = 0

   def connect(self, ip):
      return MySQLdb.connect(host=ip,
            db="test_database",
            user="perf",
            passwd="password")

   def getWriteDb(self):
      return self.master

   def getReadDb(self):
      self.currentReadDb = (self.currentReadDb + 1) % len(self.reads)
      return self.reads[self.currentReadDb]

   def executeWrite(self, query, args=None):
      db = self.getWriteDb()
      cursor = db.cursor()
      result = cursor.execute(query, args)
      db.commit()

      return result

   def get(self, key):
      db = self.getReadDb()

      cursor = db.cursor()
      cursor.execute('SELECT * from testz')
      result = cursor.fetchall()
      cursor.close()

      return result

   def insertPerson(self, person):
      pprint(person)

   def set(self, key, value):
      db = self.getWriteDb

   def update(self, key, value):
      # Update the value.
      pass
