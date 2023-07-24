from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("PartitionExample")
sc = SparkContext(conf=conf)

# Create an RDD from a list
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data, numSlices=4)  # numSlices specifies the number of partitions

# Check the number of partitions
print("Number of Partitions: ", rdd.getNumPartitions())


====================================================================================================

from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "RDDOperations")

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Transformation operations
mapped_rdd = rdd.map(lambda x: x * x)
filtered_rdd = rdd.filter(lambda x: x % 2 == 0)

# Action operations
sum_of_elements = rdd.reduce(lambda x, y: x + y)
first_element = rdd.first()

# Display the results
print("Mapped RDD: ", mapped_rdd.collect())  # Output: [1, 4, 9, 16, 25]
print("Filtered RDD: ", filtered_rdd.collect())  # Output: [2, 4]
print("Sum of elements: ", sum_of_elements)  # Output: 15
print("First element: ", first_element)  # Output: 1
