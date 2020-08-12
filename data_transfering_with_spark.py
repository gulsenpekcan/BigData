
from pyspark.sql import SparkSession
import time

'''spark = SparkSession \
    .builder \
    .appName("Python Spark SQL example") \
    .config('spark.driver.extraClassPath', '/opt/spark/jars/postgresql-42.2.14.jar') \
    .getOrCreate()

df = spark.read.jdbc('jdbc:postgresql://localhost:5432/project1', 'public.table1', properties={"user": "postgres", "password": "852456"})

#Save the dataframe to the table.
df.write.jdbc('jdbc:postgresql://localhost:5432/project1', 'public.table2', mode='overwrite', properties={"user": "postgres", "password": "852456"})'''


start = time.time()

spark = SparkSession \
        .builder \
        .appName("Transfer data with spark") \
        .config('spark.driver.extraClassPath', '/opt/spark/jars/postgresql-42.2.14.jar') \
        .getOrCreate()

df = spark.read.jdbc('jdbc:postgresql://localhost:5432/project1', 'public.data_table',
                         properties={"user": "postgres", "password": "852456"})

# Save the dataframe to the table.
df.write.jdbc('jdbc:postgresql://localhost:5432/project1', 'public.transferred_data', mode='overwrite',
                  properties={"user": "postgres", "password": "852456"})

print("Execution time: %f" % (time.time() - start))

# Execution time: 23.322607