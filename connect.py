import psycopg2
from config import load_config

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def create_table(conn, table_name, **columns):
    pass

if __name__ == '__main__':
    config = load_config()
    connect(config)