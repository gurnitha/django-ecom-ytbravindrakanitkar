# apps/core/admin.py 

# Django modules
from django.contrib import admin

# Django locals
from apps.core import models 

# Register your models here.

admin.site.register(models.Customer)