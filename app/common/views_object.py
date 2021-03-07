from django.shortcuts import render, redirect
from django import template
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from common.forms import UserConnectionForm, UserCreationForm, ChangePasswordForm, ChangeEmailForm
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, resolve_url
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormView
from django.conf import settings

class HomeView(TemplateView):

    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_query = User.objects.all()
        context['user_query'] = user_query
        return context

class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'common/inscription.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            u = User.objects.create_user(
                    form.cleaned_data.get('pseudo'),
                    form.cleaned_data.get('email'),
                    form.cleaned_data.get('password'),
                    is_active = True,
            )
            u.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

class LoginView(FormView):

  template_name = 'common/login.html'
  form_class = UserConnectionForm

  def form_valid(self, form):
    username = form.cleaned_data['pseudo']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    if user and user.is_active:
        login(self.request, user)
        return redirect('profile')
    user = User.objects.first()
    login(self.request, user)
    return HttpResponseRedirect('home')


class LogoutView(FormView):

  def get(self, request, **kwargs):

    logout(request)

    return redirect('home') 

class ProfileView(TemplateView):

    template_name = 'common/profile.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, {})

class ChangePasswordView(FormView):
    form_class = ChangePasswordForm
    template_name = 'common/change_password.html'


    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            u = request.user
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

class ChangeEmailView(FormView):
    form_class = ChangeEmailForm
    template_name = 'common/change_email.html'


    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            u = request.user
            u.email = form.cleaned_data.get('email')
            u.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})