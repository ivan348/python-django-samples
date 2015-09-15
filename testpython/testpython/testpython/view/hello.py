from django.http import HttpResponse
import datetime, os
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
	