from experiment import Experiment, DBType
from util.stats import Stats

class ReadExperiment(Experiment):
   """Simple experiment that performs some reads."""

   def main(self):
      self.getPeople(10000)
      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = ReadExperiment()
exp.main()
