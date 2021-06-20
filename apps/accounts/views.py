# apps/accounts/views.py 

# Django modules
from django.shortcuts import render
from django.contrib.auth.models import User 

# Django locals
from apps.core import models 

# Create your views here.

# Login
def user_login(request):
	return render(request, 'accounts/login.html')

# Register
def user_register(request):
	return render(request, 'accounts/register.html')

# Logout
def user_logout(request):
	pass 