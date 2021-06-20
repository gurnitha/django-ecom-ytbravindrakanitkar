# apps/core/models.py 

# Django modules 
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Customer(models.Model):

	# default django user models
	user = models.OneToOneField(
			User, 
			null=False, 
			blank=False,
			on_delete=models.CASCADE) # if user was deleted, all its data will also be deleted
	
	# extra fields add to user models fields
	phone = models.CharField(
			max_length=12,
			blank=False)


	def __str__(self):
		return self.user.username