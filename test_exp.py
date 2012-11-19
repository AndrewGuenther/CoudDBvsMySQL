from experiment import Experiment, DBType
from util.stats import Stats

class TestExperiment(Experiment):
   def main(self):
      self.insertPeople(1000)
      Stats.output()
      print "done"

exp = TestExperiment()
exp.main()
