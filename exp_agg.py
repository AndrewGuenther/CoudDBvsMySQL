from experiment import Experiment, DBType
from util.stats import Stats

class AggregateExperiment(Experiment):
   """Experiment that performs aggregates on preexisting data in the DB."""

   def main(self):
      self.runAggregates()

      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = AggregateExperiment()
exp.main()
