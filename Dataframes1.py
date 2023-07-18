from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Sample data
data = [("John", 25), ("Alice", 30), ("Bob", 20), ("Jane", 35)]

# Create DataFrame
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()


# Sort DataFrame in ascending order by Age using sort()
sorted_df = df.sort("Age")
sorted_df.show()

# Sort DataFrame in descending order by Age using sort()
sorted_df_desc = df.sort("Age", ascending=False)
sorted_df_desc.show()

# Sort DataFrame in ascending order by Age using orderBy()
sorted_df = df.orderBy("Age")
sorted_df.show()

# Sort DataFrame in descending order by Age using orderBy()
sorted_df_desc = df.orderBy(col("Age").desc())
sorted_df_desc.show()

#PySpark also supports SQL functions for sorting data
# Register DataFrame as a temporary table
df.createOrReplaceTempView("people")

# Sort DataFrame in ascending order using SQL sort function
sorted_df = spark.sql("SELECT * FROM people ORDER BY Age")
sorted_df.show()

# Sort DataFrame in descending order using SQL sort function
sorted_df_desc = spark.sql("SELECT * FROM people ORDER BY Age DESC")
sorted_df_desc.show()

