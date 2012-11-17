
class Stats(object):
   inserts = []
   updates = []
   deletes = []
   
   lookups = []
   joins = []

   @staticmethod
   def addInsert(time):
      Stats.inserts += time

   @staticmethod
   def addUpdate(time):
      Stats.updates += time

   @staticmethod
   def addDelete(time):
      Stats.deletes += time

   @staticmethod
   def addLookup(time):
      Stats.lookups += time

   @staticmethod
   def addJoin(time):
      Stats.joins += time
