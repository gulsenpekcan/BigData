import psycopg2

DB_NAME = "project1"
DB_USER = "postgres"
DB_PASS = "852456"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Database connected successfully")

except:
    print("Database not connected")