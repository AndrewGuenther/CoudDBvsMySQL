from pprint import pprint
from experiment import Experiment
from util.stats import Stats

def main():
    exp = Experiment()
    exp.insertPeople(100)
    exp.updatePeople(100)
    Stats.dump('exp1.tmp')

if __name__ == "__main__":
   main()
