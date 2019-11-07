from django import forms
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'datetime', 'location', 'address', 'city', 'state', 'image_link', 'type', 'category')