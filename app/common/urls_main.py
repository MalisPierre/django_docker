from django.conf.urls import include, url
from common import views_main
from django.urls import path

urlpatterns = [
    path('home', views_main.home, name='home'),
    path('connect', views_main.connect, name='connect'),
]
