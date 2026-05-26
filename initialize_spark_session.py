from pyspark.sql import SparkSession

from pyspark.sql import functions as f

spark = SparkSession.builder.\
appName("demo").\
getOrCreate()

data = [(1,"Gowthu","2,5,10,11"),(2,"priya","10,15,20,25")]

df = spark.createDataFrame(data,["id", "name", "marks"]) \
    .withColumn("split", f.split(f.col("marks"),","))

df.show()

df.printSchema()

print(" spark session")


