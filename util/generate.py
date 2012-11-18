import sys
import json
import random

# Enum for sex
FEMALE = 0
MALE = 1

# Global ID counter
ID = 0

# Load boy, girl, and surnames into memory
f = open('boys.txt', 'r')
boyNames = [e.strip() for e in f.readlines()]
f.close()

f = open('girls.txt', 'r')
girlNames = [e.strip() for e in f.readlines()]
f.close()

f = open('surnames.txt', 'r')
surnames = [e.strip() for e in f.readlines()]
f.close()

# Generate a random given name
def randomGivenName(sex):
   return random.choice(girlNames) if sex == FEMALE else random.choice(boyNames)

# Generate a random surname
def randomSurname():
   return random.choice(surnames)

# Create a random person
def buildPerson(maleParent = None, femaleParent = None):
   # Increment ID counter
   global ID
   ID += 1

   # Define a person with the given parents and ID
   person = {
               'id':           ID,
               'maleParent':   None if maleParent is None else maleParent['id'],
               'femaleParent': None if femaleParent is None else femaleParent['id']
               'age':          random.randint(1, 85)
            }

   # Pick a sex for the person
   person['sex'] = random.randint(FEMALE, MALE)

   # Pick a surname for the person
   person['surname'] = randomGivenName(person['sex'])

   # If a male parent is defined, inherit their given name, if not, pick one at random
   if maleParent is not None:
      person["givenName"] = maleParent["givenName"]
   else:
      person["givenName"] = randomSurname()

   return person     
      
# Generate a set of random people starting with a given number of ancestors and then reproduce for
# a given number of generations
def generate(ancestors, generations):
   # Lists to hold the current generation
   males = []
   females = []

   # Create the first generation
   for _ in range(1, ancestors):
      # Create a person
      person = buildPerson()

      # Place person in appropriate sex list. If sex is not recognized, raise exception.
      if person['sex'] == MALE:
         males.append(person)
      elif person['sex'] == FEMALE:
         females.append(person)
      else:
         raise NameError('Unknown sex: '+person['sex'])

   # Create following generations
   for _ in range(0, generations):
      # Shuffle the current generation
      random.shuffle(males)
      random.shuffle(females)

      for i in range(0, min(len(males), len(females))):
         # Create a person
         person = buildPerson(males[i], females[i])

         # Place person in appropriate sex list. If sex is not recognized, raise exception.
         if person['sex'] == MALE:
            males.append(person)
         elif person['sex'] == FEMALE:
            females.append(person)
         else:
            raise NameError('Unknown sex: '+person['sex'])

   print males
   print females

if __name__ == "__main__":
   if len(sys.argv) != 3:
      print "Usage:"
      print "   python generate.py [NUMBER OF ANCESTORS] [NUMBER OF GENERATIONS]"
   else:
      generate(int(sys.argv[1]), int(sys.argv[2]))
