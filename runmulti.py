import sys
import subprocess

try:
   script = sys.argv[1]
   numChildren = int(sys.argv[2])
except:
   print "Usage: %s <num children>" % sys.argv[0]
   sys.exit()

for i in range(0, numChildren):
   subprocess.call(["python", script])

print "no more children"
