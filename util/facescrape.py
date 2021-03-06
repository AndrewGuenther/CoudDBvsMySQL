import urllib, urllib2
import ast, json, time
from couchbase.client import Couchbase

backoff = 10

#000000 -> 004600
#100000 -> 101634

# returns dic if successful
def getFace(id):
   url = "http://graph.facebook.com/"+str(id)+"/"
   req = urllib2.Request(url, None, {"User-Agent":"Magic Browser"})
   global backoff

   try:
      # Get request from web
      face =  ast.literal_eval(urllib2.urlopen(req).read())
      backoff = 10
      return face
   except Exception, e:
      print e
      if '403' in str(e):
        print 'sleeping for:', backoff
        time.sleep(backoff)
        backoff = backoff*2
      return None

def scrapeId(id,bucket):
    face = getFace(id)
    if (face):
        print 'Inserted ' + face["name"]
        bucket.set(str(id), 0, 0, json.dumps(face))

def main():
    import sys
    if len(sys.argv) < 2:
        print "Usage: facescrape <startID> [<endID>]"
        sys.exit(1)
   
    start = int(sys.argv[1])
    if len(sys.argv) < 3:
        end = start + 1
    else:
        end = int(sys.argv[2])

    # ip bucket pass
    couchbase = Couchbase("ip-10-168-7-254.us-west-1.compute.internal:8091", "facebook", "")
    print 'connected to couchbase...'
    bucket = couchbase["facebook"]
    
    for id in range(start,end):
        print id
        scrapeId(id, bucket)
        time.sleep(0.1)

if __name__ == "__main__":
   main()