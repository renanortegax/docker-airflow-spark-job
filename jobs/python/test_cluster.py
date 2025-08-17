from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

def main():
    spark = SparkSession.builder \
        .appName("TestClusterParallelism") \
        .getOrCreate()
        
    df = spark.range(1, 1_000_001)
    # forcando 8 particoes pra ver a divisao nos 2 workers
    df = df.repartition(8)

    # fazendo algumas contagens/agregacao pra ver a divisao dos workers
    total = df.count()
    print(f"Total de linhas: {total:,}")
    soma = df.agg(_sum(col("id"))).collect()[0][0]
    print(f"Soma de todos os números: {soma:,}")
    
    grouped = df.withColumn("resto", col("id") % 10).groupBy("resto").count()
    grouped.show()

    spark.stop()

if __name__ == "__main__":
    main()
