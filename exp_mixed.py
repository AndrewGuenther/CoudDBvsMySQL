from experiment import Experiment, DBType
from util.stats import Stats

class MixedExperiment(Experiment):
   """Experiment that performs an even number of reads and writes."""

   def main(self):
      for _ in range(0, 1000):
         # updatePeople performs an equal number of reads and writes.
         self.updatePeople(5, True, True)

      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = MixedExperiment()
exp.main()
