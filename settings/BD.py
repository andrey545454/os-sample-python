# Работа с бд (конкретнее с PostgreSQL)
import psycopg2
from os import environ


# подключаемся к бд
def connect():
    conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'),
                            user=environ.get('POSTGRESQL_USER'),
                            password=environ.get('POSTGRESQL_PASSWORD'),
                            host=environ.get('POSTGRESQL_SERVICE_HOST'))
    cur = conn.cursor()
    return cur


def get_info():
    """достаём информацию из бд"""
    cur = connect()
    cur.execute('Select * from bd;')
    return cur.fetchall()
