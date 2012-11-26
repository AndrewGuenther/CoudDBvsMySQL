from multiprocessing import Pool, Lock
import sys
import subprocess
from util.stats import Stats
import glob
import os

"""Script that forks processes and runs the same experiment multiple times.

   Arguments:
      experiment file:
         Name of python file that consists of an experiment.

      db name:
         The name of the database to run tests on. Currently only mysql or couchbase.

      num children:
         Number of children to spawn.

      machine number:
         The machine number for the current run of tests. This determines the
         offset for valid personid's so each machine should have a unique machine
         number to run tests.

      experiment offset:
         The number of people already inserted into the database.
         The first run for inserts would be 0. After inserting 10,000 people
         the offset would be 10000."""

# Clear stats directory.
for f in glob.glob('stats/*.dump'):
   os.unlink (f)

try:
   script = sys.argv[1]
   db = sys.argv[2]
   numChildren = int(sys.argv[3])
   machineNumber = int(sys.argv[4])
   expOffset = int(sys.argv[5])

   # Set the global offset to one more than machine number times a billion.
   globalOffset = machineNumber * 1000000000 + 1
except:
   print "Usage: %s <experiment file> <db name> <num children> <machine number> <experiment offset>" % sys.argv[0]
   sys.exit()

def launchChild(number):
   processOffset = number * 100000000
   start = globalOffset + processOffset
   end = start + expOffset

   print "launching %s with start = %s and end = %s" % (number, start, end)

   subprocess.call(["python", script, db, str(start), str(end)])

# Launch children and block until they finish.
pool = Pool(processes = numChildren)
pool.map(launchChild, range(0, numChildren))

fpath = os.path.dirname(__file__)
dumps = glob.glob(os.path.join(fpath, "stats/*.dump"))

Stats.load(*dumps)
Stats.output()
