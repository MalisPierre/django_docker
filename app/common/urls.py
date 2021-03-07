from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('base/', include ('common.urls_main')),
    path('object/', include ('common.urls_object'))
]
