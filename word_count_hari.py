from pyspark.sql import SparkSession
from pyspark.sql import functions as f

def word_count():
    spark = SparkSession \
                .builder \
                .master("local") \
                .appName("dd") \
                .getOrCreate()
    
    data = [("hi",), ("hi hello",), ("hi hello hello",)]

    df = spark.createDataFrame(data, ["data"])

    words_df = df.withColumn("words", f.split(f.col("data"), " ")).drop("data")

    word_df = words_df.withColumn("word", f.explode(f.col("words"))).drop("words")

    count_df = word_df.groupBy("word").count()

    count_df.show()

    count_df.explain(True)

    spark.stop()











    
    