import psycopg2
from os import environ

print(environ.get('POSTGRESQL_DATABASE'), environ.get('POSTGRESQL_USER'),environ.get('POSTGRESQL_PASSWORD'),environ.get('POSTGRESQL_SERVICE_HOST'))

conn = psycopg2.connect(dbname=environ.get('POSTGRESQL_DATABASE'), user=environ.get('POSTGRESQL_USER'), password=environ.get('POSTGRESQL_PASSWORD'), host=environ.get('POSTGRESQL_SERVICE_HOST'))
cur = conn.cursor()
cur.execute('SELECT * FROM bd;')
print(cur.fetchall())
cur.close()
conn.close()