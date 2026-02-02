from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("SmokeTest") \
    .getOrCreate()

print("Spark version:", spark.version)

spark.range(10).show()

spark.stop()
