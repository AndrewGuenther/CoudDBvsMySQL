import time
import pickle

class Stats(object):
   ops = {}

   # Execute and time the given method
   @staticmethod
   def execute(fun, args):
      # Run and time function call
      t1 = time.time()
      res = fun(*args)
      t2 = time.time()

      # If the function has never been run before, initialize a list for it in the ops dict
      if Stats.ops.get(fun.__name__, None) is None:
         Stats.ops[fun.__name__] = []

      # Append response time to its respective list
      Stats.ops[fun.__name__].append(t2 - t1)

      # Return function result
      return res

   @staticmethod
   def output():
      maxLen = 18
      sumTime = 0
      print "{0:{width}} |{1:{width}} |{2:{width}} |{3:{width}}".format("Function", "Run count", "Average time", "Total time", width=maxLen)
      print "{0:-<{width}}".format("", width=((maxLen + 2) * 4))

      for key, value in Stats.ops.items():
         total = sum(value)
         sumTime += total
         count = len(value)
         average = total / count
         print "{0:{width}} |{1:<{width}} |{2:<{width}} |{3:<{width}}".format(key, count, average, total, width=maxLen)

      print
      print "Total execution time: {0}".format(sumTime)

   # Pickle and dump the ops dict
   @staticmethod
   def dump(filename):
      f = open(filename, 'w')
      pickle.dump(Stats.ops, f)
      f.close()

   # Load a set of serialized dumps
   @staticmethod
   def load(*filenames):
      for filename in filenames:
         f = open(filename, 'r')
         tmp = pickle.load(f)
         f.close()

         for key, val in tmp.items():
            if Stats.ops.get(key, None) is None:
               Stats.ops[key] = []

            Stats.ops[key] += val

# Testing procedure
if __name__ == "__main__":
   import os

   def add(x, y):
      return x + y

   Stats.execute(add, [1, 2])
   Stats.execute(add, [3, 4])
   Stats.execute(add, [5, 6])
   Stats.execute(add, [7, 8])
   Stats.execute(add, [9, 10])

   Stats.dump('test1.tmp')
   Stats.ops = {}

   Stats.execute(add, [1, 2])
   Stats.execute(add, [3, 4])
   Stats.execute(add, [5, 6])
   Stats.execute(add, [7, 8])
   Stats.execute(add, [9, 10])

   Stats.dump('test2.tmp')
   Stats.ops = {}

   Stats.load('test1.tmp', 'test2.tmp')

   assert len(Stats.ops[add.__name__]) == 10

   Stats.output()

   os.remove('test1.tmp')
   os.remove('test2.tmp')
