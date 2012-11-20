from experiment import Experiment, DBType
from util.stats import Stats

class MixedExperiment(Experiment):
   """Simple experiment that performs some reads and writes."""

   def main(self):
      for _ in range(0, 1000):
         # updatePeople performs an equal number of reads and writes.
         self.updatePeople(5, True, True)

      Stats.output()

exp = MixedExperiment()
exp.main()
