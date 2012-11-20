from experiment import Experiment, DBType

class ResetExperiment(Experiment):
   """Dummy class to clear the MySQL tables"""
   pass

if raw_input("Really really clear tables? [y/n]") == 'y':
   exp = ResetExperiment()
   exp.reset()
