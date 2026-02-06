from pyspark.sql import SparkSession

spark = (
    SparkSession.builder \
    .master("local[*]") \
    .appName("sparklearning") \
    .config("spark.eventLog.enabled","true") \
    .config("spark.eventLog.dir","file:///c:/spark-events") \
    .getOrCreate()
)

print("Spark version:", spark.version)

spark.range(10).show()
print("Running feature branch: add-logging")
spark.stop()
