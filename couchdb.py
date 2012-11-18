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

   def set(self, key, value):
      # Set the value.
      pass

   def update(self, key, value):
      # Update the value.
      pass
