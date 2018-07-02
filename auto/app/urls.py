from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^access_request$',views.access, name='access_request'),
    url(r'^admin$',views.admin, name='admin'),
]
