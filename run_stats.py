from util.stats import Stats
import glob
import os

fpath = os.path.dirname(__file__)
dumps = glob.glob(os.path.join(fpath, "stats/*.dump"))

Stats.load(*dumps)

Stats.output()
