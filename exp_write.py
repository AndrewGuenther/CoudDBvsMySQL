from experiment import Experiment, DBType
from util.stats import Stats

class WriteExperiment(Experiment):
   """Experiment that performs exclusively writes."""

   def main(self):
      self.insertPeople(10000)

      Stats.output()
      Stats.dump(self.getDumpFileName())

exp = WriteExperiment()
exp.main()
