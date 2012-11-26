class DB(object):
   """Base class for all database classes."""

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

   def getAgeAggregate(self):
      # Performs aggregates based on people's ages.
      pass

   def getFemaleAggregate(self):
      # Returns the number of females in the database.
      pass
