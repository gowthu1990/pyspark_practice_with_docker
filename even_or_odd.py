from pyspark.sql import SparkSession
from pyspark.sql import functions as f

def even_or_odd():

    spark = SparkSession \
                .builder \
                .master("local") \
                .appName("devenodd") \
                .getOrCreate()

    data = [(1,), (2,), (3,), (4,)]

    df = spark.createDataFrame(data, ["number"])

    new_df = df.withColumn("evenorodd", f.when(f.col("number") % 2 == 0, "even").otherwise("odd"))

    new_df.show()

    spark.stop()



