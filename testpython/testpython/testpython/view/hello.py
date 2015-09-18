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
def say(request):
	return HttpResponse(get_expenses(), content_type="application/json")
def template(request):
	os.chdir("testpython")
	print os.listdir(os.curdir)
	t = Template(open("text.txt"))
	d = dict(name="Ivan")
	return HttpResponse(t.substitute({"name": "Ivan"}))
	