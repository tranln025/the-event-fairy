from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import EventForm
from .models import Profile, Event, Invitation, Contact, Comment

# Create your views here.

########## Base Pages ##########

def test(request):
  return HttpResponse("Goodbye rocket ship. Hello Home.")

def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

########## Show Events ##########

def public_list(request):
    events = Event.objects.filter(type='Public')
    context = {'events': events, 'type': 'Public'}
    return render(request, 'event_list.html', context)

@login_required
def private_list(request):
    events = Event.objects.filter(type='Private')
    context = {'events': events, 'type': 'Private'}
    return render(request, 'event_list.html', context)

def event_detail(request,event_pk):
    event = Event.objects.get(id=event_pk)
    guests = ", ".join([invitation.guest.username for invitation in Invitation.objects.filter(event_id=event_pk)])
    context = {'event': event, 'guests': guests}
    return render(request, 'event_detail.html', context)

########## Editing Events ##########

@login_required
def event_create(request):
    if request.method == 'POST':
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['date_and_time'] = request.POST['date_and_time'].replace('T', ' ')
        request.POST._mutable = mutable
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_detail', event_pk=event.pk)
    else:
        form = EventForm()
    context = {'form':form, 'header': "Add New Event"}
    return render(request, 'event_form.html', context)

@login_required
def event_edit(request, event_pk):
    event = Event.objects.get(id=event_pk)
    if request.method == 'POST':
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['date_and_time'] = request.POST['date_and_time'].replace('T', ' ')
        request.POST._mutable = mutable
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event=form.save()
            return redirect('event_detail', event_pk=event.pk)
    else:
        form = EventForm(instance=event)
    context = {'form':form, 'header':f"Edit {event.title}"}
    return render(request, 'event_form.html', context)

@login_required
def event_delete(request, event_pk):
    event = Event.objects.get(id=event_pk)
    event.delete()
    if event.type == 'Public':
        return redirect('public_list')
    elif event.type == 'Private':
        return redirect('private_list')

########## Event Invitation ##########

@csrf_exempt
def event_invite(request, event_pk):
    event = Event.objects.get(id=event_pk)
    contacts = Contact.objects.filter(user1=request.user)
    context = {'event': event, 'contacts': contacts}
    if request.method == 'POST':
        checkedContacts_set = request.POST.getlist('checkedContacts[]') 
        for username in checkedContacts_set:
            guest = User.objects.get(username=username)
            invitation = Invitation.objects.create(event=event, guest=guest)
        return redirect('event_detail', event_pk=event.pk)
    else:
        return render(request, 'invite_form.html', context)