from experiment import Experiment, DBType
from util.stats import Stats

class AggregateExperiment(Experiment):
   """Simple experiment that performs some reads."""

   def main(self):
      self.runAggregates()
      Stats.output()

exp = AggregateExperiment()
exp.main()
