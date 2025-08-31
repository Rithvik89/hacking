from pyspark.sql import SparkSession
import time
import psutil
import os

## Spark Session builds a connection to spark driver..
## Then we use that spark context to create RDDs and execution also does not happen until an action is called.
## For all the transformations, Spark builds a logical plan and only when an action is called, it optimizes and executes the plan.
## Here we are using the RDD API to perform a word count operation.

## Steps 1-4 does not trigger execution. They are lazily evaluated. Even these were segregated into 2 stages :
## Stage 1 - Read, Transform (lines, words, word_pairs) : Map
## Stage 2 - Reduce (word_pairs, word_counts) : Here set of words are assigned to a executor (Shuffle Phase)
## Action 5 triggers the execution.

spark = SparkSession.builder.appName("WordCountRDD").getOrCreate()
sc = spark.sparkContext

files = ["500MBfile.txt", "1GBfile.txt", "2GBfile.txt"]

process = psutil.Process(os.getpid())

for file in files:
    start_time = time.time()

    # 1. Load file into an RDD
    lines = sc.textFile(file)

    # 2. Split lines into words (flatMap)
    words = lines.flatMap(lambda line: line.split(" "))

    # 3. Map each word to (word, 1)
    word_pairs = words.map(lambda word: (word, 1))

    # 4. Reduce by key to count
    word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

    # 5. Collect results
    results = word_counts.collect()


    end_cpu = process.cpu_percent(interval=None)
    end_mem = process.memory_info().rss

    print(f"CPU percent: {end_cpu}%")
    print(f"Memory used: {end_mem / (1024 * 1024):.2f} MB")

    print(f"Unique words in {file}: {len(results)}")
    print(f"Time taken for {file}: {time.time() - start_time} seconds")
