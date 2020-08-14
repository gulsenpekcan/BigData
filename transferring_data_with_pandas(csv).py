import d6tstack.utils
import pandas as pd
import time
# from sqlalchemy import create_engine


conn = 'postgresql+psycopg2://postgres:852456@localhost:5432/project1'

start = time.time()

path_csv = '/home/guls/Desktop/data_df.csv'

pd.read_sql_table('data_table', con=conn).to_csv(path_csv, index=False)
print("Successfully wrote to csv")

data = pd.read_csv(path_csv, sep=',')
d6tstack.utils.pd_to_psql(data, conn, 'transferred_data3', if_exists='replace')

print("Execution time: %f" % (time.time() - start))

# Execution time: 14.760243
