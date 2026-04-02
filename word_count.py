import os
import shutil
from pyspark.sql import SparkSession
from pyspark.sql import functions as f

# 1. Define Paths (These point to the mounted Docker Volume)
DATA_DIR = "/app/data"
INPUT_FILE = f"{DATA_DIR}/words.txt"
OUTPUT_DIR = f"{DATA_DIR}/words_output"

# 2. Initialize Spark
spark = SparkSession.builder.appName("WordCounter").getOrCreate()

# 3. READ (Parse the data)
df = spark.read.csv(INPUT_FILE, header=False, inferSchema=True)
print("\n[Parse] Raw Data in PySpark:")
df.show()

# 5. PROCESS (Transform the data)
processed_df = df.withColumn("splits", f.split(f.col("_c0"), " ")) \
                 .withColumn("word", f.explode(f.col("splits"))) \
                 .groupBy("word") \
                 .count()


print("\n[Process] Transformed Data:")
processed_df.show()

# 6. SAVE (Load the data back out)
# Clean up the output directory if you are running this multiple times
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)

# Write the data as JSON (Simulating writing to a curated GCS bucket)
# In GCP, this could also be .format("bigquery").save("project.dataset.table")
processed_df.write.mode("overwrite").json(OUTPUT_DIR)
print(f"[Load] Processed data saved to: {OUTPUT_DIR}\n")

spark.stop()