#Spark provides APIs in multiple programming languages. The primary ones are Scala, Java, Python, and R.
#Here's an example using the Python AP

from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SparkExample") \
    .getOrCreate()

# Read data from a file
data = spark.read.csv("input_file.csv", header=True)

# Perform transformations and actions on the data using Spark API
result = data.select("column1", "column2").groupBy("column1").agg({"column2": "avg"})

# Display the result
result.show()
