# apps/accounts/views.py 

# Django modules
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout

# Django locals
from apps.core import models 

# Create your views here.

# Login
def user_login(request):

	# jika form disubmit atau Login button diklik
	if request.method == "POST":	
		username 	= request.POST.get('username')
		password 	= request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None: # if the user is known 
			login(request,user)
			return redirect('/')

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

		# # Testing
		# print(username, email, password, confirm_password, phone)

		# Create and save user jika password == confirm_password
		if password == confirm_password:

			# Check if user already exists
			if User.objects.filter(username=username).exists():
				print('Username already exists')
				return redirect('user_register')

			# Check if email already exists
			else:
				if User.objects.filter(email=email).exists():
					print('Email already exists')
					return redirect('user_register')

				# Save user  
				else:	
					user = User.objects.create_user(
						username=username,
						email=email,
						password=password)
					user.save()
					data = models.Customer(user=user,phone=phone)
					data.save()

					# Log in the use after successfully registered 
					registered_user = authenticate(username=username,password=password)
					if registered_user is not None: # if registered_user is known
						login(request, user)
						return redirect('/')

		# Error
		else:
			print("Error here ...")
			return redirect('user_register')

	return render(request, 'accounts/register.html')


# Logout
def user_logout(request):
	logout(request) 
	return redirect('/')