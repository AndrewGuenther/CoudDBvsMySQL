from experiment import Experiment, DBType
from util.stats import Stats

class ReadParentsExperiment(Experiment):
   """Experiment that performs exclusively reads by getting people and
      their parents."""

   def main(self):
      self.getPeopleAndParents(10000)

      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = ReadParentsExperiment()
exp.main()
