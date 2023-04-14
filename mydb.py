# install mysql on your computer
# pip install mysql
#pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'kennyde1st'
)

# prepare a cursor object
cursorObject = database.cursor()

#c Create a database
cursorObject.execute("CREATE DATABASE ladel")

print("All Done")