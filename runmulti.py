import sys
import subprocess

try:
   script = sys.argv[1]
   db = sys.argv[2]
   numChildren = int(sys.argv[3])
except:
   print "Usage: %s <script file> <mysql|couchbase> <num children>" % sys.argv[0]
   sys.exit()

for i in range(0, numChildren):
   subprocess.call(["python", script, db, str(i * 10000)])

print "Done spawning children!"
