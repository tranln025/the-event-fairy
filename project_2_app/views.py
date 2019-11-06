from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.decorators import login_required

# Create your views here.


def test(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")







def landing(request):
    return render(request, 'landing.html')





def about(request):
    return render(request, 'about.html')







def register(request):
    return render(request, 'register.html')






def login(request):
    return render(request, 'login.html')



def logout(request):
    return redirect('landing')




def home(request):
    return render(request, 'home.html')



########## Show Events ##########


def public_list(request):
    return render(request, 'event_list.html')


def private_list(request):
    return render(request, 'event_list.html')



def event_detail(request):
    return render(request, 'event_detail.html')




########## Editing Events ##########


def event_create(request):
    return render(request, 'event_form.html')




def event_edit(request):
    return render(request, 'event_form.html')




def event_delete(request):
    return render(request, 'event_form.html')






########## Show Profile ##########

def profile(request):
    return render(request, 'profile.html')


