from experiment import Experiment, DBType
from util.stats import Stats

class TestExperiment(Experiment):
   """Simple test experiment that performs some reads."""

   def main(self):
      self.getPeople(10)
      Stats.output()
      print "done"

exp = TestExperiment()
exp.main()
