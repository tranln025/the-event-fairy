from django.urls import path
from . import views



urlpatterns = [
    path('',views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('events/public/',views.public_list, name='public_list'),
    path('events/private',views.private_list, name='private_list'),
    path('events/<int:event_pk>/',views.event_detail, name='event_detail'),
    path('events/new/',views.event_create, name='event_create'),
    path('events/<int:event_pk>/edit/',views.event_edit, name='event_edit'),
    path('events/<int:event_pk>/delete/',views.event_delete, name='event_delete'),
]