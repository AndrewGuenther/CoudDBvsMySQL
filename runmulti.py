from multiprocessing import Pool, Lock
import sys
import subprocess

try:
   script = sys.argv[1]
   db = sys.argv[2]
   numChildren = int(sys.argv[3])
   machineNumber = int(sys.argv[4])
   expOffset = int(sys.argv[5])

   # Set the global offset to one more than machine number times a billion.
   globalOffset = machineNumber * 1000000000 + 1
except:
   print "Usage: %s <script file> <mysql|couchbase> <num children> <machine number> <experiment offset>" % sys.argv[0]
   sys.exit()

def launchChild(number):
   processOffset = number * 250000000
   start = globalOffset + processOffset
   end = start + expOffset

   print "launching %s with start = %s and end = %s" % (number, start, end)

   subprocess.call(["python", script, db, str(start), str(end)])

pool = Pool(processes = numChildren)
pool.map(launchChild, range(0, numChildren))
