from django import forms
from django.forms.widgets import DateTimeInput

from . models import Event, Profile

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date_and_time', 'location', 'address', 'city', 'state', 'image_link', 'type', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'date_and_time': DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'location': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'address': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'city': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'state': forms.Select(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'image_link': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'type': forms.Select(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
            'category': forms.TextInput(attrs={'class': 'form-control col-md-6', 'style': 'margin: 0 auto'}),
        }

class ProfPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image_link',)
        widgets = {
            'image_link': forms.TextInput(attrs={'class': 'form-control col'})
        }