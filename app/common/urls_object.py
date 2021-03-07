from django.conf.urls import include, url
from django.urls import path
from django.views.generic import TemplateView
from common.views_object import HomeView, LoginView, LogoutView, ProfileView, SignUpView, ChangePasswordView, ChangeEmailView

urlpatterns = [
	path('home', HomeView.as_view(), name='home_object'),
	path('inscription', SignUpView.as_view(), name='inscription'),
	path('change_password', ChangePasswordView.as_view(), name='change_password'),
	path('change_email', ChangeEmailView.as_view(), name='change_email'),
	path('profile', ProfileView.as_view(), name='profile'),
	path('login', LoginView.as_view(), name='login'),
	path('logout', LogoutView.as_view(), name='logout'),
]
