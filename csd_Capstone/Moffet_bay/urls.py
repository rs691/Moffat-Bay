from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
      path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
      # path('account/', sign_in_up, name='sign_in_up'),
      path('', views.index , name='index'),
      path('success/', views.success, name='success'),
       path('reservation/', views.reservation, name='reservation'),
       path('about/', views.about, name='about'),
       path('profile/', views.profile, name='profile'),
       path('contact/', views.contact, name='contact'),
       path('reservation_summary/', views.reservation_summary, name='reservation_summary'),
     
    #    path('sign_in/', auth_views.LoginView.as_view(), name='sign_in'),
      
        path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
