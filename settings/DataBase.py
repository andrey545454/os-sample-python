import MySQLdb
from os import environ

MYSQL_SERVICE_HOST = environ.get('MYSQL_SERVICE_HOST')
MYSQL_USER = environ.get('MYSQL_USER')
MYSQL_PASSWORD = environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE = environ.get('MYSQL_DATABASE')

conn = MySQLdb.connect(host=MYSQL_SERVICE_HOST, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DATABASE)
cursor = conn.cursor()

cursor.execute("SELECT * FROM Info")

# Получаем данные.
row = cursor.fetchone()
print(row)