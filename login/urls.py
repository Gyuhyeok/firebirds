from django.conf.urls import url
from . import views
from django.contrib import auth
from django.contrib.auth import views

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login'),
	#url(r'^logout/$', logout_page),
	

]