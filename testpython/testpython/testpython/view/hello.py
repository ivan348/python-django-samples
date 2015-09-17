from django.http import HttpResponse
from string import Template
import datetime, os
from testpython.model.db import get_expenses
class Car:
	def __init__(self, color, speed):
		self.color = color
		self.speed = speed
	def getInfo(self):
		return self.color + "   " + self.speed

def car(request, s):
	c = Car("green", s)
	return HttpResponse(c.getInfo())
def home(request):
    html = "<html><body>It is now %d.</body></html>" % 1
    return HttpResponse(html)
def say():
	return HttpResponse(get_expenses())
def template(request):
	t = Template("hello $name")
	d = dict(name="Ivan")
	print(say())
	return HttpResponse(t.substitute({"name": "Ivan"}))
	