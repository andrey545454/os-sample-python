import psycopg2
from os import environ

conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'),
                        user=environ.get('POSTGRESQL_USER'),
                        password=environ.get('POSTGRESQL_PASSWORD'),
                        host=environ.get('POSTGRESQL_SERVICE_HOST'))
cur = conn.cursor()
cur.execute('Select * from bd;')
for row in cur:
    print(row)
cur.close()
conn.close()