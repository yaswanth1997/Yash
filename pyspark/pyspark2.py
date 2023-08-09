# the two types - hash and range partitioners
from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("PartitionerExample")
sc = SparkContext(conf=conf)

# RDD with key-value pairs
data = sc.parallelize([(1, "apple"), (2, "banana"), (3, "orange"), (4, "grape")])

# Hash partitioning
hash_partitioned_data = data.partitionBy(2)

# Range partitioning
range_partitioned_data = data.sortByKey().partitionBy(2)

# Get the partitioner used in each RDD
hash_partitioner = hash_partitioned_data.partitioner
range_partitioner = range_partitioned_data.partitioner

print("Hash Partitioner: ", hash_partitioner)
print("Range Partitioner: ", range_partitioner)
