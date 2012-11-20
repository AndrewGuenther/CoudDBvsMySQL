from experiment import Experiment, DBType
from util.stats import Stats

class WriteExperiment(Experiment):
   """Simple experiment that performs some writes."""

   def main(self):
      self.insertPeople(10000)
      Stats.output()

exp = WriteExperiment()
exp.main()
