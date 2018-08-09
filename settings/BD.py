import psycopg2
from os import environ

conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'),user=environ.get('POSTGRESQL_USER'), password=environ.get('POSTGRESQL_PASSWORD'), host=environ.get('POSTGRESQL_SERVICE_HOST'))
cur = conn.cursor()
cur.execute("SELECT 1 FROM pg_database WHERE datname='{}'".format(environ.get('POSTGRESQL_DATABASE')))
print(cur.fetchone())
cur.close()
conn.close()