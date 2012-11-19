from pprint import pprint
from util.personbuffer import PersonBuffer
from db.mysqldb import MySqlDb
from db.couchdb import CouchDB

class DBType(object):
    MYSQL, COUCHBASE = range(2)

class Experiment(object):
    """docstring for Experiment"""
    def __init__(self, dbType=1, resetDB=False):
        super(Experiment, self).__init__()
        self.insertedIds = []
        self.dbType = dbType
        self.connect()

        if resetDB:
            self.reset()

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
        if (self.dbType == DBType.MYSQL):
            schema = open('schema.sql').read()
            schemaStatements = schema.split(';\n')
            for statement in schemaStatements:
                if statement:
                    self.db.executeWrite(statement)
        #TODO add reset for couch

    def insertPeople(self, number):
        for _ in range(number):
            person = PersonBuffer.getNewPerson()
            self.db.insertPerson(person)
            self.insertedIds.append(person['id'])

    def getPeople(self, number):
        if number > len(self.insertedIds):
            print 'Only ', len(self.insertedIds), ' people have been inserted.'
            number = len(self.insertedIds)

        ret = []
        for i in range(number):
            personid = self.insertedIds[i]
            ret.append(self.db.getPerson(personid)[0])

        return ret

    def updatePeople(self, number):
        if number > len(self.insertedIds):
            print 'Only ', len(self.insertedIds), ' people have been inserted.'
            number = len(self.insertedIds)

        people = self.getPeople(number)

        for person in people:
            if person['age']:
                person['age'] += 1
            else:
                person['age'] = 1
            ret.append(self.db.updatePerson(person))