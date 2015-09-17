import mysql.connector
def get_expenses():
	res = []
	try:
		con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='expenses')
		cursor = con.cursor()
		cursor.execute("SELECT * FROM expenses")
		res = cursor.fetchone()
		con.close()
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		    print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
		    print("Database does not exist")
		else:
		    print(err)
	else:
	  	con.close()
	return res