# 1. Official Apache Spark image
FROM apache/spark:latest

USER root

# 2. Create a symlink so 'python' works
RUN ln -s /usr/bin/python3 /usr/bin/python

WORKDIR /app

# 4. Copy your local script
COPY ./src /app/src

# 5. Use the official spark-submit to run the script
ENTRYPOINT [ "/opt/spark/bin/spark-submit" ]

CMD ["/app/src/practice/pyspark_practice/practice_20260905/main.py"]