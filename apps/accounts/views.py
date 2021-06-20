# apps/accounts/views.py 

# Django modules
from django.shortcuts import render
from django.contrib.auth.models import User 

# Django locals
from apps.core import models 

# Create your views here.

# Login
def user_login(request):

	# jika form disubmit button diklik
	if request.method == "POST":	
		pass 
		
	return render(request, 'accounts/login.html')


# Register
def user_register(request):

	# Jika form disubmit atau Register button diklik
	if request.method == "POST":
		"""Ambil username, email, password, 
		confirm_password dan nomor telpon"""
		username 	= request.POST.get('username')
		email 		= request.POST.get('email')
		password 	= request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		phone 		= request.POST.get('phone')

		# Testing
		print(username, email, password, confirm_password, phone)

	return render(request, 'accounts/register.html')


# Logout
def user_logout(request):
	pass 