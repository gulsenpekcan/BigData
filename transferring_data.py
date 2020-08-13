
import string
import random
import psycopg2

DB_NAME = "project1"
DB_USER = "postgres"
DB_PASS = "852456"
DB_HOST = "localhost"
DB_PORT = "5432"


def rand_data_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_and_insert_data():
    commands = (
        """
        CREATE TABLE transferred_data2 (
            id serial PRIMARY KEY,
            data VARCHAR(255) NOT NULL
        )
        """)

    sql = "INSERT INTO transferred_data2 (data) VALUES (%s)"
    data_list = []

    conn = None
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
        print("Database connected successfully")

        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)

        cur.close()
        # commit the changes
        conn.commit()
        print("Table(s) created successfully")

        '''cur = conn.cursor()

        for _ in range(100000):
            rand_data = rand_data_generator()
            cur.execute(sql, (rand_data,))

        # commit the changes to the database
        conn.commit()
        print("Data inserted successfully")'''
        # close communication with the PostgreSQL database server
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    generate_and_insert_data()



