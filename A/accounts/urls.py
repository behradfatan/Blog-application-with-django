from django.urls import path
from . import views

urlpatterns = [
    path('user_login/', views.user_login, name="user_login"),
    path('register/', views.user_register, name="register"),
    path('logout/', views.user_logout, name="logout"),
]