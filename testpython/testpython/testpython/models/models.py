from django.db import models

class Expense(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField()
	value = models.CharField()
	type = models.CharField()
	currency = models.CharField()
	category = models.CharField()
	
	class Meta:
 	    db_table = "expenses"
