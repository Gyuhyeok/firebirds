from django.conf.urls import url, patterns
from freeboard.views import board

urlpatterns = [
	url(r'^$', board),
	
]
