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
    return cur, conn


def get_info(name):
    """достаём информацию из бд"""
    cur, conn = connect()
    cur.execute('Select * from %(name)s;', {'name': name})
    return cur.fetchall()


def set_info(name, link):
    """добавляем информацию в бд"""
    cur, conn = connect()
    cur.execute('INSERT INTO bd (name, link, count) Values (%(name)s, %(link)s, %(count)s)', {'name': name,
                                                                                              'link': link,
                                                                                              'count': 1})
    conn.commit()


def update_info(count, link):
    """обновляем информацию в бд"""
    cur, conn = connect()
    cur.execute('UPDATE bd SET count=(%(count)s) WHERE link=(%(link)s)', {'count': count+1,
                                                                          'link': link})
    conn.commit()
