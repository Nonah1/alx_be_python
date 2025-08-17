import mysql.connector
from mysql.connector import errorcode

try:
	conn =  mysql.connector.connect (
		host = "localhost",
		user = "root",
		password = "root123",
)

	cursor = conn.cursor()
	
	cursor.execute ("CREATE DATABASE IF NOT EXISTS alx_book_store")
	print ("Database 'alx_book_store' created successfully! ")

except mysql.connector.Error as err:
	print (f"Error: {err}")

finally:
	if 'cursor' in locals() and cursor:
		cursor.close()
	if 'conn' in locals() and conn.is_connected:
		conn.close()