from django.contrib import admin
from .models import Profile, Event, Invitation, Contact, Comment
# Register your models here.


admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Invitation)
admin.site.register(Contact)
admin.site.register(Comment)