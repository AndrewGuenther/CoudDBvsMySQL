from db import DB
from couchbase.client import Couchbase
from couchbase.rest_client import RestConnection

class CouchDB(DB):
   def __init__(self):
      self.client = Couchbase("ip-10-168-7-254.us-west-1.compute.internal:8091",
            "genealogy",
            "")
      self.bucket = self.client['genealogy']

   def get(self, key):
      # Get the value.
      return self.bucket.get(key)

   def insertPerson(self, person):
      self.set(str(person['id']), person)

   def set(self, key, value, expiry=0, flags=0):
      # Set the value.
      return self.bucket.set(key, expiry, flags, value)

   def update(self, key, value):
      # Update the value.
      pass
