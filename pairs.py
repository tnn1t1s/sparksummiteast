## Imports

from pyspark import SparkConf, SparkContext

## CONSTANTS

APP_NAME = "My Spark Application"

##OTHER FUNCTIONS/CLASSES

## Main functionality

def main(sc):
	rdd = sc.parallelize(range(1000), 10)
	print rdd.mean()

if __name__ == "__main__":
	conf = SparkConf().setAppName(APP_NAME)
	conf = conf.setMaster("local[*]")
	sc   = SparkContext(conf=conf)
	main(sc)
