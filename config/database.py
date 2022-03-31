import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    password = '',
    user = 'root',
    database = 'base_image',
    port = 3306
)
db.autocommit=True