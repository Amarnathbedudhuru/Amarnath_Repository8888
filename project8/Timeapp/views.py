from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
import datetime

def display_time(request):

	server_time=datetime.datetime.now()

	return HttpResponse(server_time)



	
