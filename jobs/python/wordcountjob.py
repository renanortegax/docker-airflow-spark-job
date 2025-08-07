from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark_word_count").getOrCreate()

text = "isso se trata apenas de um teste que estou fazendo pra ver se a esse teste funciona mesmo ou trata de um teste que nao funciona"

words = spark.sparkContext.parallelize(text.split(" "))

word_count = words.map(lambda x: (x,1)).reduceByKey(lambda a, b: a + b) # pega como se fosse a chave e valor e soma

# print(word_count.collect())

for w in word_count.collect():
    print(f"{w[0]}: {w[1]}")
    
spark.stop()