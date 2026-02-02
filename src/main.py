from pyspark.sql import SparkSession

spark = (
    SparkSession.builder \
    .master("local[*]") \
    .appName("SmokeTest") \
    .config("spark.eventLog.enabled","true") \
    .config("spark.eventLog.dir","file:///c:/spark-events") \
    .getOrCreate()
)

print("Spark version:", spark.version)

spark.range(10).show()
print("Running feature branch: add-logging")
spark.range(20).show(5)

spark.stop()
