class DB(object):
   def insertPerson(self, person):
      # Insert a person into the database.
      pass

   def getPerson(self, personid):
      # Retrieve the specified person.
      pass

   def getPersonAndParents(self, personid):
      # Retrieve the specified person and their parents.
      pass

   def updatePerson(self, person):
      # Updates the existing row associated with the given person.
      pass

   def getAggregate(self, filterDict):
      # Gets a count of the person entries with the given attributes (in filterDict)
      pass