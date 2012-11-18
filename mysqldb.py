from db import DB
import MySQLdb

class MySqlDb(DB):
   def __init__(self):
      self.db = MySQLdb.connect(host="ip-10-168-7-254.us-west-1.compute.internal",
            db="test_database",
            user="perf",
            passwd="password");

   def get(self, key):
      # Get the value.
      pass

   def set(self, key, value):
      # Set the value.
      pass

   def update(self, key, value):
      # Update the value.
      pass
