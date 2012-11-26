import sys
from experiment import Experiment, DBType

class ResetExperiment(Experiment):
   """Dummy class to clear the DB."""
   pass

if len(sys.argv) < 2:
   print "Usage: %s <mysql|couchbase>" % sys.argv[0]
   sys.exit()

if raw_input("Really really drop all data? [y/n]") == 'y':
   exp = ResetExperiment()
   exp.reset()
