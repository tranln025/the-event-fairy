from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from project_2_app.models import Profile, Contact, Invitation, Event
from project_2_app.forms import ProfPicForm

# Create your views here.

########## Auth ##########

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'register.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error':'That email already exists.'}
                    return render(request, 'register.html', context)
                else: 
                    user = User.objects.create_user(
                    username=username_form, 
                    email=email_form, 
                    password=password, 
                    first_name=first_name, 
                    last_name=last_name,
                    )
                    user.save()
                    return redirect('home')
        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username_form = request.POST['username']
        password_form = request.POST['password']
        user = auth.authenticate(username = username_form, password=password_form)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            context = {'error': 'Invalid Credentials'}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('landing')

########## Profile Contents ##########
        
@login_required
def profile(request):
    user = request.user
    username = user.username
    contacts = Contact.objects.filter(user1=user)
    created_events = user.events.all()
    if request.method == 'POST':
        form = ProfPicForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(user_id = user.id, image_link = request.POST['image_link'])
            return redirect('profile')
    else:
        form = ProfPicForm()
        context = {'user': user, 'username': username, 'form': form, 'created_events': created_events, 'contacts': contacts}
        if Profile.objects.filter(user_id=user.id).exists():
            profile = Profile.objects.get(user_id=user.id)
            prof_pic_link = profile.image_link    
            context['prof_pic_link'] = prof_pic_link
        if Invitation.objects.filter(guest=request.user, confirmation=True).exists():
            confirmed_invitations = Invitation.objects.filter(guest=request.user, confirmation=True)
            for invitation in confirmed_invitations:
                event_id = invitation.event_id
                going_events = Event.objects.filter(id=event_id)
                context['going_events'] = going_events
    return render(request, 'profile.html', context)

@login_required
def prof_pic_edit(request):
    user = request.user
    username = user.username
    profile = Profile.objects.get(user_id=user.id)
    prof_pic_link = profile.image_link    
    created_events = user.events.all()
    invited_events = Invitation.objects.filter(guest=user)
    contacts = Contact.objects.filter(user1=user)
    if request.method == 'POST':
        form = ProfPicForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile')
    else:
        profile.image_link = ''
        profile.save()
        form = ProfPicForm()
    context = {'user': user, 'username': username, 'form': form, 'created_events': created_events, 'contacts': contacts, 'invited_events': invited_events, 'prof_pic_link': prof_pic_link}
    return render(request, 'profile.html', context)

########## Contacts ##########

@login_required
def contacts_list(request):
    contacts = Contact.objects.filter(user1=request.user)
    for contact in contacts:
        print(contact.user2.username)
    context = {'contacts': contacts}
    return render(request, 'contacts_list.html', context)

@login_required
@csrf_exempt
def contact_add(request):
    if request.method == 'POST':
        username = request.POST['user2']
        if User.objects.filter(username__iexact=username).exists():
            found_user = User.objects.get(username__iexact=username)
            if Contact.objects.filter(user1_id=request.user, user2_id=found_user):
                context = {'error': f"You have already added {found_user.username} as a contact."}
                return render(request, 'contact_form.html', context)
            elif found_user == request.user:
                context = {'error': 'You cannot add yourself as a contact.'}
                return render(request, 'contact_form.html', context)
            else:
                new_contact = Contact.objects.create(user1=request.user, user2=found_user)
                return redirect('profile')
        else:
            context = {'error': 'Username does not exist. Please try again.'}
            return render(request, 'contact_form.html', context)
    else:
        return render(request, 'contact_form.html')

@login_required
def contact_delete(request, contact_pk):
    Contact.objects.get(id=contact_pk).delete()
    return redirect('profile')