from db import DB
import MySQLdb

class MySqlDb(DB):
   def __init__(self):
      self.master = self.connect("ip-10-168-7-254.us-west-1.compute.internal")

      self.reads = []
      self.reads.append(self.connect("ip-10-168-7-254.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-160-183-128.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-160-90-29.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-168-111-37.us-west-1.compute.internal"))

   def connect(self, ip):
      return MySQLdb.connect(host=ip,
            db="test_database",
            user="perf",
            passwd="password");

   def get(self, key):
      # Get the value.
      values = []

      for db in self.reads:
         cursor = db.cursor()
         cursor.execute('SELECT * from testz');
         values.append(cursor.fetchall())

      return values

   def set(self, key, value):
      # Set the value.
      pass

   def update(self, key, value):
      # Update the value.
      pass
