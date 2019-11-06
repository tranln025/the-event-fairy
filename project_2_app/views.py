from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.decorators import login_required

# Create your views here.


def test(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")