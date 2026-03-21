# PySpark_Practice_With_Docker (PySpark Local Setup with Docker)

## Project Overview

This project provides a foundational template for setting up and running **Apache Spark (PySpark)** locally using **Docker**. It is designed to offer a fully containerized, reproducible environment for practicing PySpark development, bypassing common local installation hurdles and OS-specific limitations. The repository includes a basic "Hello World" application that validates the setup by initializing a Spark session, generating a sample DataFrame, and executing it using `spark-submit`.

### Tech Stack
* **Engine:** Apache Spark (Latest Version) 
* **Language:** Python (Compatible version as per the Apache Spark version)
* **Runtime:** Docker (Linux-based)

---

## Getting Started

### Prerequisites
* Docker Desktop installed and running.
* 4GB+ RAM allocated to Docker.

### 1. Build the Image
The Dockerfile handles the JDK installation, PySpark libraries, and the necessary symlinks for the Python runtime.
```bash
docker build -t pyspark-practice .
```

### 2. Execute the Benchmark
Run the container to trigger the Spark job. The container uses spark-submit as the entrypoint for production-grade execution.

```bash
docker run --rm pyspark-practice
```
