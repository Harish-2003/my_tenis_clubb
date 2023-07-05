from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('loginpage',views.loginpage,name='login'),
    path('main/', views.main, name='main'),
    path('main/members/data/<int:id>',views.details,name='details'),
    path('main/members/', views.members, name='members'),
]
