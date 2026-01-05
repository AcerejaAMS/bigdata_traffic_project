from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

spark = SparkSession.builder.appName("TrafficClustering").getOrCreate()

data = spark.read.csv("hdfs://master:9000/traffic_data/traffic_data.csv", header=True, inferSchema=True)

assembler = VectorAssembler(
    inputCols=["speed", "vehicle_count"],
    outputCol="features"
)

features = assembler.transform(data)

kmeans = KMeans(k=3, seed=1)
model = kmeans.fit(features)

predictions = model.transform(features)

predictions.select("speed", "vehicle_count", "prediction") \
    .write.csv("hdfs://master:9000/traffic_predictions", header=True)
