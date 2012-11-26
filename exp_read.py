from experiment import Experiment, DBType
from util.stats import Stats

class ReadExperiment(Experiment):
   """Experiment that performs exclusively reads."""

   def main(self):
      self.getPeople(10000)

      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = ReadExperiment()
exp.main()
