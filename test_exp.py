from experiment import Experiment, DBType
from util.stats import Stats

class TestExperiment(Experiment):
   def main(self):
      self.insertPeople(10)
      Stats.output()
      print "done"

exp = TestExperiment()
exp.main()
