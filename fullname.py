from pyspark.sql import SparkSession
from pyspark.sql import functions as f

def merge_name():
    spark = SparkSession \
                .builder \
                .master("local") \
                .appName("demo") \
                .getOrCreate()
    

    data = [("hari", "Priya"), ("Sai", "Gowtham")]
    df = spark.createDataFrame(data,["firstname", "lastname"])
    mergedf = df.withColumn("fullname", f.concat(f.col("firstname"), f.lit(" ") , f.col("lastname"))).drop("firstname", "lastname")
    mergedf.show()

    spark.stop()
                
