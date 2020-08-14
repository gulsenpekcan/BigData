
import psycopg2
import time

DB_NAME = "project1"
DB_USER = "postgres"
DB_PASS = "852456"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
print("Database connected successfully")

cur = conn.cursor()

start = time.time()

# Set up a variable to store our file path and name.
path_f = "/home/guls/Desktop/data.csv"

with open(path_f, 'w') as f_output:
    cur.copy_to(f_output, 'public.data_table', sep=',')

conn.commit()

SQL_for_file = '''COPY public.transferred_data2 FROM STDIN WITH CSV'''
with open(path_f, 'r') as f:
    cur.copy_expert(SQL_for_file, f)

conn.commit()

print("Execution time: %f" % (time.time() - start))

'''
SQL_for_file = "COPY ({0}) TO STDOUT WITH CSV HEADER".format("SELECT * FROM public.data_table")

with open(path_f, 'w') as f_output:
cur.copy_expert(SQL_for_file, f_output)

conn.commit()

with open(path_f, 'r') as f:
    next(f)  #Skip the header row.
    cur.copy_from(f, 'public.transferred_data2', sep=',')

conn.commit()'''

cur.close()

# Execution time: 4.819338
