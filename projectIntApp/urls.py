from django.conf.urls import url
from django.urls import path,include
from . import views

urlpatterns = [
   # url('users/', views.UserCreate.as_view(), name='account-create'),
     path('',views.welcome),
     path('register/',views.register),
     path('status/',views.status),
     path('login/',views.login,name='login')
]