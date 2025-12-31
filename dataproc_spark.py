# Dataproc Spark job skeleton
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('dataproc-job').getOrCreate()
df = spark.read.csv('gs://your-bucket/path/*.csv', header=True, inferSchema=True)
df.write.parquet('gs://your-bucket/processed/')
