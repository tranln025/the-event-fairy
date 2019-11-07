from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')



class Event(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=15)
    category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_invitations')
    guest = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='guest_invitations')
    confirmation = models.BooleanField(default=False)
    date_invited = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    user1 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user1_contacts')
    user2 = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user2_contacts')
    date_added = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author_comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)