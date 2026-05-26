from pyspark.sql import SparkSession

spark = SparkSession.builder\
.master("local")\
.appName("demo")\
.getOrCreate()

print("hello world")