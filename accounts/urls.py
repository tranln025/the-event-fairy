from django.urls import path

from . import views



urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/contacts/', views.contacts_list, name='contacts_list'),
    path('profile/contacts/new/', views.contact_add, name='contact_add')
]