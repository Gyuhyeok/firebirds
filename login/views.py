from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
# Create your views here.
def login(request):
	return render(request, 'login/logintemp.html')	

def logout(request):
	logout(request)
	return HttpResponseRedirect('/')



