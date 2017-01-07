## Imports

from pyspark import SparkConf, SparkContext

## CONSTANTS

APP_NAME = "My Spark Application"

##OTHER FUNCTIONS/CLASSES

## Main functionality

def main(sc):
	 x = sc.parallelize([("a", 1), ("b", 4)])
	 y = sc.parallelize([("a", 2)])
	 print sorted(x.cogroup(y).collect())

if __name__ == "__main__":
	conf = SparkConf().setAppName(APP_NAME)
	conf = conf.setMaster("local[*]")
	sc   = SparkContext(conf=conf)
	main(sc)
