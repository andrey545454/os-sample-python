import psycopg2
from os import environ

conn = psycopg2.connect(dbname=environ('POSTGRESQL_DATABASE'), user=environ('POSTGRESQL_USER'), password=environ('POSTGRESQL_PASSWORD'), host=environ('POSTGRESQL_SERVICE_HOST'))
cur = conn.cursor()
cur.execute('SELECT * FROM bd;')
print(cur.fetchall())
cur.close()
conn.close()