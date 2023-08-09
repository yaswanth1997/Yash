#Spark provides built-in functions to read data from various formats
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataReadExample") \
    .getOrCreate()

# Read CSV data
df_csv = spark.read.csv("data.csv", header=True)

# Read JSON data
df_json = spark.read.json("data.json")

# Read XML data (XML format is not natively supported, you can use third-party libraries)
df_xml = spark.read.format("com.databricks.spark.xml") \
    .option("rowTag", "record") \
    .load("data.xml")

# Read Parquet data
df_parquet = spark.read.parquet("data.parquet")

df.show()