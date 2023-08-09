#(repartition and coalesce are used to control the number of partitions in an RDD or DataFrame.

#repartition: It is used to increase or decrease the number of partitions. It shuffles the data and can be used to balance the data across partitions.

#coalesce: It reduces the number of partitions without shuffling the data. It is more efficient than repartition when decreasing the number of partitions.

#Use repartition when you want to increase the number of partitions or need to perform a full data shuffle. Use coalesce when you want to decrease the number of partitions without a full shuffle
from pyspark import SparkContext

sc = SparkContext("local", "RepartitionCoalesceExample")

# Create an RDD
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rdd = sc.parallelize(data, numSlices=4)  # 4 partitions

# Repartition to 8 partitions
repartitioned_rdd = rdd.repartition(8)
print("Repartitioned RDD: ", repartitioned_rdd.glom().collect())

# Coalesce to 2 partitions
coalesced_rdd = rdd.coalesce(2)
print("Coalesced RDD: ", coalesced_rdd.glom().collect())
