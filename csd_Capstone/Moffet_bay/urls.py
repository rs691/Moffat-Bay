from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('projects/', views.projects, name='projects'),
   
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    
]