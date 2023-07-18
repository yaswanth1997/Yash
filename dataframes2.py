#using the sort() function in PySpark to sort a DataFrame and the distinct() function to remove duplicate rows
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35), ("Alice", 25), ("Dave", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Sort the DataFrame by "Age" column in ascending order
sorted_df = df.sort("Age")

# Remove duplicate rows
distinct_df = sorted_df.distinct()

# Show the result
distinct_df.show()

df = df.sort("Age").distinct()
