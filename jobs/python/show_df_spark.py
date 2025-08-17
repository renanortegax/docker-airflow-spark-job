from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("CreateDataFrameExample").getOrCreate()

data_tuples = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
df_tuples = spark.createDataFrame(data_tuples, ["Name", "Age"])
df_tuples.show()

print("="*60)
print("="*23, " FINALIZADO ", "="*23)
print("="*60)

spark.stop()