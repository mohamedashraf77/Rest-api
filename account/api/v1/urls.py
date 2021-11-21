from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
  path('login', obtain_auth_token, name= 'api-login'),
  path('signup', views.signup, name= 'signup'),
  path('logout', views.logout, name= 'logout'),
]