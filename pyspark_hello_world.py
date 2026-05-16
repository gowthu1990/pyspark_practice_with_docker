from pyspark.sql import SparkSession

def pyspark_hello_world():
    spark = SparkSession.builder \
        .appName("Architect_Docker_Test") \
        .getOrCreate()

    data = [("Setup", "Successful"), ("Environment", "Containerized")]
    df = spark.createDataFrame(data, ["Step", "Status"])

    print("\n" + "="*30)
    print("SPARK IS RUNNING IN DOCKER")
    print("="*30)
    df.show()

    spark.stop()