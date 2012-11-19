from pprint import pprint

from db import DB
import MySQLdb
import MySQLdb.cursors


class MySqlDb(DB):
   def __init__(self):
      self.master = self.connect("ip-10-168-7-254.us-west-1.compute.internal")

      self.reads = []
      self.reads.append(self.master)
      self.reads.append(self.connect("ip-10-160-183-128.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-160-90-29.us-west-1.compute.internal"))
      self.reads.append(self.connect("ip-10-168-111-37.us-west-1.compute.internal"))

      # Used for round robin reads.
      self.currentReadDb = 0

   def insertPerson(self, person):
      personid = person['id']

      self.executeWrite( \
            """INSERT INTO people
               SET personid = %s,
                   surname = %s,
                   givenName = %s,
                   femaleParent = %s,
                   maleParent = %s,
                   sex = %s,
                   age = %s""",
            (personid,
             person['surname'],
             person['givenName'],
             person['femaleParent'],
             person['maleParent'],
             person['sex'],
             person['age']))

      for address in person['address']:
         addressid = self.insertAddress(address)

         self.executeWrite( \
               """INSERT INTO people_addresses
                  SET personid = %s,
                      addressid = %s,
                      isPrimary = %s""",
               (personid,
                addressid,
                1 if address['isPrimary'] else 0))

      for education in person['education']:
         educationid = self.insertEducation(education)

         self.executeWrite( \
               """INSERT INTO people_education
                  SET personid = %s,
                      educationid = %s""",
               (personid,
                educationid))

   def getPerson(self, personid):
      return self.executeSelect( \
            """SELECT * FROM people
               LEFT JOIN people_addresses pa USING (personid)
               LEFT JOIN addresses a1 ON (pa.addressid = a1.addressid)
               LEFT JOIN people_education pe USING (personid)
               LEFT JOIN education e USING (educationid)
               LEFT JOIN addresses a2 ON (e.addressid = a2.addressid)
               WHERE personid = %s""",
            (personid))

   def getPersonAndParents(self, personid):
      return self.executeSelect( \
            """SELECT * FROM people p
               LEFT JOIN people_addresses pa USING (personid)
               LEFT JOIN addresses a1 ON (pa.addressid = a1.addressid)
               LEFT JOIN people_education pe USING (personid)
               LEFT JOIN education e USING (educationid)
               LEFT JOIN addresses a2 ON (e.addressid = a2.addressid)
               LEFT JOIN people p1 ON (p.femaleParent = p1.personid)
               LEFT JOIN people p2 ON (p.maleParent = p2.personid)
               WHERE p.personid = %s""",
            (personid))

   def updatePerson(self, person):
      self.executeWrite( \
            """UPDATE people
               SET surname = %s,
                   givenName = %s,
                   femaleParent = %s,
                   maleParent = %s,
                   sex = %s,
                   age = %s
               WHERE personid = %s""",
            (person['surname'],
             person['givenName'],
             person['femaleParent'],
             person['maleParent'],
             person['sex'],
             person['age'],
             person['id']))
      pass

   def connect(self, ip):
      return MySQLdb.connect(host=ip,
            db="genealogy",
            user="perf",
            passwd="password",
            cursorclass=MySQLdb.cursors.DictCursor)

   def getWriteDb(self):
      return self.master

   def getReadDb(self):
      self.currentReadDb = (self.currentReadDb + 1) % len(self.reads)
      return self.reads[self.currentReadDb]

   def executeWrite(self, query, args=None):
      db = self.getWriteDb()
      cursor = db.cursor()
      result = {}

      result['affectedRows'] = cursor.execute(query, args)
      result['lastrowid'] = cursor.lastrowid

      db.commit()

      return result

   def executeSelect(self, query, args=None):
      db = self.getReadDb()
      cursor = db.cursor()

      cursor.execute(query, args)

      result = cursor.fetchall()
      cursor.close()

      return result

   def insertAddress(self, address):
      return self.executeWrite( \
            """INSERT INTO addresses
               SET line1 = %s,
                   line2 = %s,
                   city = %s,
                   state = %s,
                   country = %s,
                   zip = %s""",
            (address.get('line1', None),
             address.get('line2', None),
             address.get('city', None),
             address.get('state', None),
             address.get('country', None),
             address.get('zip', None)))['lastrowid']

   def insertEducation(self, education):
      addressid = self.insertAddress(education['address'])

      return self.executeWrite( \
            """INSERT INTO education
               SET institution = %s,
                   level = %s,
                   addressid = %s""",
            (education['institution'],
             education['level'],
             addressid))['lastrowid']
