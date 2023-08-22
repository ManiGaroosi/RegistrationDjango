from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage , name='HomePage'),
    path('register/', views.RigisterPage , name='register'),
    path('login/', views.LoginPage , name='login'),
]