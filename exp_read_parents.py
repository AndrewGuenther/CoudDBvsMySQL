from experiment import Experiment, DBType
from util.stats import Stats

class ReadParentsExperiment(Experiment):
   """Simple experiment that gets people and their parents."""

   def main(self):
      self.getPeopleAndParents(10000)
      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = ReadParentsExperiment()
exp.main()
