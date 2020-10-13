import psycopg2
import sys

def connectwithPostgreSQL():
    try:
        conn = psycopg2.connect(
            user = "postgres",
            password = "root",
            host = "localhost",
            port = 5432,
            database = "record"
            )
        print("Connected")
    except psycopg2.Error as e:
        print(f"Error while connecting to Postgres Platform: {e}")
        sys.exit(1)

    return conn
