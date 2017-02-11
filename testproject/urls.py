
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),                           # default for admin interface
    url(r'^accounts/login/$', views.login, name='login'),       # for login required
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),  #for logout
    url(r'', include('blog.urls')),
    
]
