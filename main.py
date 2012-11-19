import sys, time
from pprint import pprint
from experiment import Experiment
from util.stats import Stats

if dbType else sys.argv[1]

def main():
    if len(sys.argv) > 1:
        dbType = int(sys.argv[1])
        exp = Experiment(dbType)
    else:
        exp = Experiment()
    exp.insertPeople(100)
    exp.updatePeople(100)
    time.sleep(1)
    Stats.dump('exp1.tmp')

if __name__ == "__main__":
   main()
