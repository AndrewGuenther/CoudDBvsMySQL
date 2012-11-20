from experiment import Experiment, DBType
from util.stats import Stats

class ReadExperiment(Experiment):
   """Simple experiment that performs some reads."""

   def main(self):
      self.getPeople(5000)
      self.getPeopleAndParents(5000)
      Stats.output()

exp = ReadExperiment()
exp.main()
