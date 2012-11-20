import sys
from experiment import Experiment, DBType

class ResetExperiment(Experiment):
   """Dummy class to clear the MySQL tables"""
   pass

if len(sys.argv) < 2:
   print "Usage: %s mysql" % sys.argv[0]
   sys.exit()

if raw_input("Really really clear tables? [y/n]") == 'y':
   exp = ResetExperiment()
   exp.reset()
