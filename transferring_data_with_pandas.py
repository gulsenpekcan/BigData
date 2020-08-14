
import pandas as pd
import time
from sqlalchemy import create_engine


# create_engine('postgresql+psycopg2://myuser:mypwd@localhost:5432/mydb')
conn = create_engine('postgresql+psycopg2://postgres:852456@localhost:5432/project1')
print("Database connected successfully")

start = time.time()

query = "SELECT * FROM public.data_table;"
df = pd.read_sql(query, conn)

df.to_sql(name='transferred_data3', con=conn, if_exists='replace', index=False)

print("Execution time: %f" % (time.time() - start))

# Execution time: 240.810781
