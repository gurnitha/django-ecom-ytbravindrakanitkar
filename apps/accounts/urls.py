# app/accounts/urls.py 

# Django modules
from django.urls import path

# Django locals
from apps.accounts import views 

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
]