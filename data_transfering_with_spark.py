
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL example") \
    .config('spark.driver.extraClassPath', '/opt/spark/jars/postgresql-42.2.14.jar') \
    .getOrCreate()

df = spark.read.jdbc('jdbc:postgresql://localhost:5432/project1', 'public.table1', properties={"user": "postgres", "password": "852456"})

#Save the dataframe to the table.
df.write.jdbc('jdbc:postgresql://localhost:5432/project1', 'public.table2', mode='overwrite', properties={"user": "postgres", "password": "852456"})

