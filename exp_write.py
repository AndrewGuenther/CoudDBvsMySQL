from experiment import Experiment, DBType
from util.stats import Stats

class TestExperiment(Experiment):
   """Simple test experiment that performs some writes."""

   def main(self):
      self.insertPeople(10000)
      Stats.output()
      print "done"

exp = TestExperiment()
exp.main()
