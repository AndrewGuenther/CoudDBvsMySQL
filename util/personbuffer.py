from generate import generate

class PersonBuffer(object):
   buffer = []
   ANCESTORS = 50
   GENERATIONS = 10

   @staticmethod
   def getNewPerson():
      if len(PersonBuffer.buffer) > 0:
         return PersonBuffer.buffer.pop(0)
      else:
         PersonBuffer.buffer = generate(PersonBuffer.ANCESTORS, PersonBuffer.GENERATIONS)
         return PersonBuffer.getNewPerson()

   @staticmethod
   def getPerson():
      pass

if __name__ == "__main__":
   print PersonBuffer.getNewPerson()
