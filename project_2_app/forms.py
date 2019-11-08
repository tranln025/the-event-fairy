from django import forms
from . models import Event, Contact, Profile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'datetime', 'location', 'address', 'city', 'state', 'image_link', 'type', 'category')

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ('user2',)

class ProfPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_link',)