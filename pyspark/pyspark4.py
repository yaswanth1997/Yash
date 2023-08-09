from pyspark import SparkContext

sc = SparkContext("local", "MapVsFlatMapExample")

data = ["hello world", "spark is awesome"]
rdd = sc.parallelize(data)

# map example
mapped_rdd = rdd.map(lambda x: x.split(" "))
print("Mapped RDD: ", mapped_rdd.collect())
# Output: [['hello', 'world'], ['spark', 'is', 'awesome']]

# flatMap example
flat_mapped_rdd = rdd.flatMap(lambda x: x.split(" "))
print("Flat Mapped RDD: ", flat_mapped_rdd.collect())
# Output: ['hello', 'world', 'spark', 'is', 'awesome']

#map: It applies a function to each element of the RDD and returns a new RDD where each element is the result of the function applied to the original element. The number of output elements is the same as the number of input elements.

#flatMap: It is similar to map, but the function returns an iterator of elements (a sequence) for each input element. The elements of these iterators are then flattened into the output RDD. The number of output elements can be different from the number of input elements.