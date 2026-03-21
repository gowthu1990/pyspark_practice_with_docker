# 1. Official Apache Spark image
FROM apache/spark:latest

USER root

# 2. Create a symlink so 'python' works
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app

# 4. Copy your local script
COPY pyspark_hello_world.py .

# 5. Use the official spark-submit to run the script
ENTRYPOINT [ "/opt/spark/bin/spark-submit" ]
CMD [ "pyspark_hello_world.py" ]