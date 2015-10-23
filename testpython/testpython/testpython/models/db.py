import mysql.connector
from testpython.models.models import Expense
from django.core import serializers
# class Expense(object):
# 	def __init__(self, id, name, value, type, currency, category):
# 		self.id = id
# 		self.name = name
# 		self.value = value
# 		self.type = type
# 		self.currency = currency
# 		self.category = category

def get_expenses():
	res = Expense.objects.all()
	# res = []
	# try:
	# 	con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='expenses')
	# 	cursor = con.cursor()
	# 	cursor.execute("SELECT id, name, value, type, currency, category FROM expenses")
	# 	for row in cursor:
	# 		r = list(row)
	# 		expense = Expense(r[0], r[1], r[2], r[3], r[4], r[5])
	# 		res.append(expense)
	# 	con.close()
	# except mysql.connector.Error as err:
	# 	print(err)
	# else:
	#   	con.close()
	# return json.dumps(res, default=lambda o: o.__dict__)
	return serializers.serialize("json", res)