from django.conf.urls import url, include
from django.contrib import admin, auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^board/', include('freeboard.urls')),
    url(r'^login/', include('login.urls')),
    
]
