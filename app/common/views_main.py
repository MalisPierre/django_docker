from django.shortcuts import render, redirect
from django import template


from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def home(request):

    user_query = User.objects.all()
    return render(request, 'common/home.html', {'user_query': user_query})

def connect(request):

    user_query = User.objects.all()
    return render(request, 'common/home.html', {'user_query': user_query})