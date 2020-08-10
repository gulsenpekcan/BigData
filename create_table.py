#!/usr/bin/python

import psycopg2

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE table1 (
            col1 VARCHAR(255) NOT NULL,
            col2 VARCHAR(255) NOT NULL,
            col3 VARCHAR(255) NOT NULL,
            col4 VARCHAR(255) NOT NULL,
            col5 VARCHAR(255) NOT NULL
        )
        """,
        """ 
        CREATE TABLE table2 (
            col1 VARCHAR(255) NOT NULL,
            col2 VARCHAR(255) NOT NULL,
            col3 VARCHAR(255) NOT NULL,
            col4 VARCHAR(255) NOT NULL,
            col5 VARCHAR(255) NOT NULL
        )
        """)

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

        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()