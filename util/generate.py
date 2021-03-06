import sys
import os
import random

class PersonGenerator(object):
   """Randomly generates lots of people for inserting/updating."""

   # Enum for sex
   FEMALE = 0
   MALE = 1

   ID = 1

   # Get the current path
   fpath = os.path.dirname(__file__)

   # Load boy, girl, and surnames into memory
   f = open(os.path.join(fpath, 'txt', 'boys.txt'), 'r')
   boyNames = [e.strip() for e in f.readlines()]
   f.close()

   f = open(os.path.join(fpath, 'txt', 'girls.txt'), 'r')
   girlNames = [e.strip() for e in f.readlines()]
   f.close()

   f = open(os.path.join(fpath, 'txt', 'surnames.txt'), 'r')
   surnames = [e.strip() for e in f.readlines()]
   f.close()

   f = open(os.path.join(fpath, 'txt', 'states.txt'), 'r')
   states = [e.strip() for e in f.readlines()]
   f.close()

   # Generate a random given name
   @staticmethod
   def randomGivenName(sex):
      return random.choice(PersonGenerator.girlNames) if sex == PersonGenerator.FEMALE else random.choice(PersonGenerator.boyNames)

   # Generate a random surname
   @staticmethod
   def randomSurname():
      return random.choice(PersonGenerator.surnames)

   @staticmethod
   def randomAddress(isPrimary=False):
      return {
                "line1":     str(random.randint(1000, 9999)) + " " + random.choice(PersonGenerator.surnames) + " Ave.",
                "line2":     None,
                "city":      random.choice(PersonGenerator.surnames) + "ville",
                "state":     random.choice(PersonGenerator.states),
                "country":   "United States",
                "zip":       random.randint(10000, 99999),
                "isPrimary": isPrimary
             }

   @staticmethod
   def randomEducation():
      state = random.choice(PersonGenerator.states)

      return {
                "institution": state + " State University",
                "address":     {
                                  "line1": "1 University Way",
                                  "line2": None,
                                  "city":  "University Town",
                                  "state": state,
                                  "zip":   93410
                               },
                "level":       "college"
             }

   # Create a random person
   @staticmethod
   def buildPerson(maleParent = None, femaleParent = None):
     # Define a person with the given parents and ID
      person = {
                  'id':           PersonGenerator.ID,
                  'maleParent':   None if maleParent is None else maleParent['id'],
                  'femaleParent': None if femaleParent is None else femaleParent['id'],
                  'age':          random.randint(1, 85),
                  'address':      [PersonGenerator.randomAddress(True), PersonGenerator.randomAddress()],
                  'education':    [PersonGenerator.randomEducation()]
               }

      # Pick a sex for the person
      person['sex'] = PersonGenerator.ID % 2

      # Pick a surname for the person
      person['surname'] = PersonGenerator.randomGivenName(person['sex'])

      # If a male parent is defined, inherit their given name, if not, pick one at random
      if maleParent is not None:
         person["givenName"] = maleParent["givenName"]
      else:
         person["givenName"] = PersonGenerator.randomSurname()

      PersonGenerator.ID += 1

      return person     
         
   # Generate a set of random people starting with a given number of ancestors and then reproduce for
   # a given number of generations
   @staticmethod
   def generate(ancestors, generations):
      # Lists to hold the current generation
      people = []

      # Create the first generation
      newGeneration = []

      for _ in range(0, ancestors):
         # Create a person
         person = PersonGenerator.buildPerson()

         # Place person in appropriate sex list. If sex is not recognized, raise exception.
         newGeneration.append(person)

      people += newGeneration

      # Create following generations
      for _ in range(0, generations):
         # Shuffle the current generation
         random.shuffle(newGeneration)

         males = [w for w in newGeneration if w["sex"] is PersonGenerator.MALE]
         females = [w for w in newGeneration if w["sex"] is PersonGenerator.FEMALE]

         newGeneration = []

         for i in range(0, min(len(males), len(females))):
            # Create a person
            person = PersonGenerator.buildPerson(males[i], females[i])

            newGeneration.append(person)

         people += newGeneration

      return people

if __name__ == "__main__":
   if len(sys.argv) != 3:
      print "Usage:"
      print "   python generate.py [NUMBER OF ANCESTORS] [NUMBER OF GENERATIONS]"
   else:
      for p in PersonGenerator.generate(int(sys.argv[1]), int(sys.argv[2])):
         print p
         print
