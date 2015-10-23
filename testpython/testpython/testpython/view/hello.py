from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from testpython.models.db import get_expenses
class Car:
	def __init__(self, color, speed):
		self.color = color
		self.speed = speed
	def getInfo(self):
		return self.color + "   " + self.speed

def car(request, s):
	c = Car("green", s)
	return HttpResponse(c.getInfo())
def settings(request):
    return render(request, "settings.html")
def say(request):
	return HttpResponse(get_expenses(), content_type="application/json")
def home(request):
	d = dict(name="Smith")
	return render(request, "home.html", d)
	