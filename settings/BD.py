import psycopg2

conn = psycopg2.connect(dbname='BD', user='andrey545454', password='andrey545454', host='10.129.104.250', port='5432')
cur = conn.cursor()
cur.execute("SELECT * FROM BD;")

print(cur.fetchall())
cur.close()
conn.close()