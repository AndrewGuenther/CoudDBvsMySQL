from experiment import Experiment, DBType

class TestExperiment(Experiment):
   def main(self):
      self.insertPeople(5)
      print "done"

exp = TestExperiment()
exp.main()
