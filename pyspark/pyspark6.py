#You can allocate resources for a Spark job by configuring various parameters like memory, cores, and executor instances. This can be done either through the Spark configuration or by using spark-submit with appropriate flags.
#using spark-submit:
spark-submit --master yarn \
             --deploy-mode cluster \
             --executor-memory 4G \
             --executor-cores 2 \
             --num-executors 5 \
             your_spark_job.py
======================================================================================================================================================================================================================================================================
#Save modes in Spark define how to handle data when saving DataFrames to external storage like HDFS or databases. Some common save modes are:

#append: Append the data to an existing data set.
#overwrite: Overwrite the existing data set.
#ignore: Ignore the save operation if data already exists.
#error (default): Throw an error if data already exists.

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SaveModeExample") \
    .getOrCreate()

# Read data from a source
data = spark.read.csv("input_file.csv", header=True)

# Save data to a target with a specific save mode
data.write.mode("overwrite").parquet("output_data.parquet")
==========================================================================================================================================================================================================
#Read modes in Spark define how to handle the behavior when reading data from external storage like HDFS or databases. Some common read modes are:

#permissive: Sets all fields to null when encountering a corrupted record during reading.
#dropMalformed: Drops the corrupted records during reading.
#failFast: Raises an exception when encountering a corrupted record during reading (default).

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ReadModeExample") \
    .getOrCreate()

# Read data from a source with a specific read mode
data = spark.read.option("mode", "permissive").csv("input_file.csv", header=True)
