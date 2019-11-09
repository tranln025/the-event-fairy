from django import forms
from django.forms.widgets import DateTimeInput

from . models import Event, Profile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'date_and_time', 'location', 'address', 'city', 'state', 'image_link', 'type', 'category')
        widgets = {'date_and_time': DateTimeInput(attrs={'type': 'datetime-local'}),}

class ProfPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_link',)