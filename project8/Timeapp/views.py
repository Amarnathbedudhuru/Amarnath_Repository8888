from django.shortcuts import render

# Create your views here.
import datetime

def display_time(request):

	server_time=datetime.datetime.now()

	dict={'time':server_time}



	return render(request=request, template_name='Timeapp/time.html',context=dict)
