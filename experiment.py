import sys
import random
from util.personbuffer import PersonBuffer
from util.generate import PersonGenerator
from util.stats import Stats
from db.mysqldb import MySqlDb
from db.couchdb import CouchDB

class DBType(object):
    MYSQL, COUCHBASE = ('mysql', 'couchbase')

class Experiment(object):
    """docstring for Experiment"""
    def __init__(self, dbType=None):
        super(Experiment, self).__init__()
        if dbType:
            self.dbType = dbType
        elif len(sys.argv) > 1:
            self.dbType = sys.argv[1]
        else:
            self.dbType = None

        self.db = None
        self.connect()

        if len(sys.argv) > 3:
            # Start and end of existing inserted values.
            self.startValues = int(sys.argv[2])
            self.endValues = int(sys.argv[3])
        elif len(sys.argv) > 2:
            self.endValues = int(sys.argv[2])
        else:
            self.endValues = 1000

        PersonGenerator.ID = self.endValues

    def connect(self):
        try:
            if (self.dbType == DBType.MYSQL):
                self.db = MySqlDb()
            elif (self.dbType == DBType.COUCHBASE):
                self.db = CouchDB()
            else:
                print 'Error: Unknown DB type... defaulting to Couchbase'
                self.db = CouchDB()
                self.dbType = DBType.COUCHBASE
        except Exception, e:
            print 'Error connecting to DB: ', e

    def reset(self):
        # Drop all tables and start from scratch.
        if self.dbType == DBType.MYSQL:
            schema = open('db/schema.sql').read()
            schemaStatements = schema.split(';\n')
            for statement in schemaStatements:
                if statement:
                    self.db.executeWrite(statement)
        elif self.dbType == DBType.COUCHBASE:
           self.db.clear()

    def getRandomPersonid(self):
      # One less because we don't want it to be inclusive.
      return random.randint(self.startValues, self.endValues - 1)

    def insertPeople(self, number, recordStats=True):
        for _ in range(number):
            person = PersonBuffer.getNewPerson()
            if recordStats:
                Stats.execute(self.db.insertPerson, [person])
            else:
                self.db.insertPerson(person)

    def getPeople(self, number, recordStats=True):
        ret = []
        for i in range(number):
            personid = self.getRandomPersonid()
            if recordStats:
                person = Stats.execute(self.db.getPerson, [personid])
            else:
                person = self.db.getPerson(personid)
            ret.append(person)

        return ret

    def getPeopleAndParents(self, number, recordStats=True):
        ret = []
        for i in range(number):
            personid = self.getRandomPersonid()
            if recordStats:
                person = Stats.execute(self.db.getPersonAndParents, [personid])
            else:
                person = self.db.getPersonAndParents(personid)
            ret.append(person)

        return ret

    def updatePeople(self, number, recordStats=True, recordReadStats=False):
        people = self.getPeople(number, recordReadStats)

        for person in people:
            if person['age']:
                person['age'] += 1
            else:
                person['age'] = 1

            if recordStats:
                Stats.execute(self.db.updatePerson, [person])
            else:
                self.db.updatePerson(person)

    def runAggregates(self, recordStats=True):
        Stats.execute(self.db.getAgeAggregate, [])

        Stats.execute(self.db.getFemaleAggregate, [])

    def getDumpFileName(self):
        return "stats/stats.%s.%s" % (self.startValues, self.endValues)
