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
      path('attractions/', views.attractions, name='attractions'),

      path('reservation_summary/', views.reservation_summary, name='reservation_summary'),
     
    #    path('sign_in/', auth_views.LoginView.as_view(), name='sign_in'),
      
      path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
     
       path('docs/', views.docs_view, name='docs'),
       path('reservation_lookup/', views.reservation_lookup, name='reservation_lookup'),
        path('my-reservations/', views.reservation_history, name='reservation_history'),
    path('past-reservations/', views.past_reservations, name='past_reservations'),
    path('future-reservations/', views.future_reservations, name='future_reservations'),
    path('create-reservation/', views.create_reservation, name='create_reservation'),
   path('room_rates/', views.room_rates, name='room_rates'),
    path('reservation-lookup/', views.reservation_lookup, name='reservation_lookup'),
    path('reservation_lookup_results/', views.reservation_lookup_results, name='reservation_lookup_results'),
    
   
       
      
     
]

