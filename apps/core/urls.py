# apps/core/urls.py 

# Django modules
from django.urls import path

# Django locals
from apps.core import views 

urlpatterns = [
    path('', views.index, name='home'),
]