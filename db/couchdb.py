import json
from db import DB
from couchbase.client import Couchbase
from couchbase.rest_client import RestConnection

class CouchDB(DB):
   def __init__(self):
      self.client = Couchbase("ip-10-168-7-254.us-west-1.compute.internal:8091",
            "genealogy",
            "")
      self.bucket = self.client['genealogy']

   def __del__(self):
      self.client = None
      self.bucket.mc_client.done()

   def insertPerson(self, person):
      self.set(str(person['id']), person)

   def getPerson(self, personid):
      if personid == None:
         return None

      return self.get(str(personid))

   def getPersonAndParents(self, personid):
      person = self.getPerson(personid)

      return (person,
            self.getPerson(person['femaleParent']),
            self.getPerson(person['maleParent']))

   def updatePerson(self, person):
      self.insertPerson(person)

   def getAgeAggregate(self):
      view = "_design/views/_view/age"
      rows = self.bucket.view(view)
      if rows:
         return rows[0]['value']
      return None

   def getFemaleAggregate(self):
      view = "_design/views/_view/females"
      rows = self.bucket.view(view)
      if rows:
         return rows[0]['value']
      return None

   def get(self, key):
      return json.loads(self.bucket.get(key)[2])

   def set(self, key, value, expiry=0, flags=0):
      return self.bucket.set(key, expiry, flags, value)

   def clear(self):
      self.bucket.flush()
