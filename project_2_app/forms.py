from django import forms
from .models import Event, Contact

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'datetime', 'location', 'address', 'city', 'state', 'image_link', 'type', 'category')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('user2',)