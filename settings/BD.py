import psycopg2
from os import environ

try:
    conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'), user=environ.get('POSTGRESQL_USER'), password=environ.get('POSTGRESQL_PASSWORD'), host=environ.get('POSTGRESQL_SERVICE_HOST'))
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM bd;')
    except:
        print('No bd')
    print(cur.fetchall())
    cur.close()
    conn.close()
except:
    print('Nope')