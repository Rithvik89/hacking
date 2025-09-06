from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Streaming").getOrCreate()


df = spark.readStream.format("socket").option("host", "localhost").option("port", 8080).load()



## Print the stream messages
query = df.writeStream.outputMode("append").format("console").start()

query.awaitTermination()
