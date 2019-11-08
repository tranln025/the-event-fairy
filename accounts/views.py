from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from project_2_app.models import Profile, Contact, Invitation
from project_2_app.forms import ProfPicForm

# Create your views here.



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
    return redirect('home')
        


def profile(request):
    user = request.user
    username = user.username
    created_events = user.events.all()
    invited_events = Invitation.objects.filter(guest=user)
    contacts = Contact.objects.filter(user1=user)
    if request.method == 'POST':
        form = ProfPicForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfPicForm()
    context = {'user': user, 'username': username, 'form': form, 'created_events': created_events, 'contacts': contacts, 'invited_events': invited_events}
    return render(request, 'profile.html', context)

def contacts_list(request):
    contacts = Contact.objects.filter(user1=request.user)
    context = {'contacts': contacts}
    return render(request, 'contacts_list.html', context)

@csrf_exempt
def contact_add(request):
    if request.method == 'POST':
        username = request.POST['user2']
        print(username)
        if User.objects.filter(username=username).exists():
            new_contact = User.objects.get(username=username)
            contact = Contact.objects.create(user1 = request.user, user2 = new_contact)
            return redirect('contacts_list')
        else:
            context = {'error': 'Username does not exist. Please try again.'}
            print(context)
            return render(request, 'contact_form.html', context)
    else:
        return render(request, 'contact_form.html')