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

df = spark.read.json("data/raw/2015-summary.json")
print("The count in the json file is:", df.count())


spark.stop()
