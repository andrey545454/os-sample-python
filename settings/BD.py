import psycopg2
from os import environ

conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'),
                        user=environ.get('POSTGRESQL_USER'),
                        password=environ.get('POSTGRESQL_PASSWORD'),
                        host=environ.get('POSTGRESQL_SERVICE_HOST'))
cur = conn.cursor()
cur.execute("\l")
cur.execute("\dt")
print(cur.fetchone())
cur.close()
conn.close()