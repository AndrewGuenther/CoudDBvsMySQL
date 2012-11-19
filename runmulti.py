from multiprocessing import Pool, Lock
import sys
import subprocess

try:
   script = sys.argv[1]
   db = sys.argv[2]
   numChildren = int(sys.argv[3])
except:
   print "Usage: %s <script file> <mysql|couchbase> <num children>" % sys.argv[0]
   sys.exit()

def launchChild(number):
   print "launching %s" % number
   subprocess.call(["python", script, db, str(number * 10000)])

pool = Pool(processes = numChildren)
pool.map(launchChild, range(0, numChildren))

print "Done spawning children!"
