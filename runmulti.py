import sys
import subprocess

try:
   numChildren = int(sys.argv[1])
except:
   print "Usage: %s <num children>" % sys.argv[0]
   sys.exit()

for i in range(0, numChildren):
   subprocess.call(["python", "runmulti.py"])

print "no more children"
