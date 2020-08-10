import string
import random
import psycopg2

def rand_data_generator(size=4, chars = string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def insert_data(data_list):
    sql = "INSERT INTO table1 (col1, col2, col3, col4, col5) VALUES (%s, %s, %s, %s, %s)"
    conn = None
    try:
        # connect to the PostgreSQL server
        DB_NAME = "project1"
        DB_USER = "postgres"
        DB_PASS = "852456"
        DB_HOST = "localhost"
        DB_PORT = "5432"

        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print("Database connected successfully")

        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, data_list)
        # commit the changes to the database
        conn.commit()
        print("Data inserted successfully")
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':

    data_list = []
    for _ in range(10000000):
        val1 = rand_data_generator()
        val2 = rand_data_generator()
        val3 = rand_data_generator()
        val4 = rand_data_generator()
        val5 = rand_data_generator()
        data_list.append((val1, val2, val3, val4, val5))

    insert_data(data_list)