from django.urls import path
from . import views



urlpatterns = [
    path('',views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('register/',views.register, name='register'),
    path('login/', views.login, name='login'),
    path('user/logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('events/public/',views.public_list, name='public_list'),
    path('events/private',views.private_list, name='private_list'),
    path('events/details',views.event_detail, name='event_detail'),
    path('events/new/',views.event_create, name='event_create'),
    path('events/edit/',views.event_edit, name='event_edit'),
    path('events/delete/',views.event_delete, name='event_delete'),
    path('user/profile',views.profile, name='profile')
]