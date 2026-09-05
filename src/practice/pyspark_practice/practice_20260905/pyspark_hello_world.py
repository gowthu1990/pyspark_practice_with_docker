from pyspark.sql import SparkSession

def hello_world():
    spark = SparkSession.builder \
                .appName("Hello World") \
                .master("local[*]") \
                .getOrCreate() 

    data = [(1, ), (2, ), (3, )]
    df = spark.createDataFrame(data, ["numbers"])
    df.show()
    spark.stop()