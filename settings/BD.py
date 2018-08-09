# Работа с бд (конкретнее с PostgreSQL)
import psycopg2
from os import environ

# подключаемся к бд
conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'),
                        user=environ.get('POSTGRESQL_USER'),
                        password=environ.get('POSTGRESQL_PASSWORD'),
                        host=environ.get('POSTGRESQL_SERVICE_HOST'))
cur = conn.cursor()


def get_info():
    """достаём информацию из бд"""
    cur.execute('Select * from bd;')
    for row in cur:
        return row

cur.close()
conn.close()