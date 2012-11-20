from generate import PersonGenerator
import random

class PersonBuffer(object):
   buffer = []
   ANCESTORS = 50
   GENERATIONS = 10

   @staticmethod
   def getNewPerson():
      if len(PersonBuffer.buffer) > 0:
         return PersonBuffer.buffer.pop(0)
      else:
         PersonBuffer.buffer = PersonGenerator.generate(PersonBuffer.ANCESTORS, PersonBuffer.GENERATIONS)
         return PersonBuffer.getNewPerson()

   @staticmethod
   def getPersonID():
      return random.randint(1, PersonBuffer.buffer[0]['id'] - 1)

if __name__ == "__main__":
   print PersonBuffer.getNewPerson()
   print PersonBuffer.getPersonID()
