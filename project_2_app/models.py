from django.db import models
from django.contrib.auth.models import User

# Create your models here.
state_abbrs = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')

    def __str__(self):
        return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description provided")
    datetime = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=tuple(state_abbrs.items()), default='CA')
    image_link = models.TextField()
    # image_upload = models.ImageField(upload_to='prof_images/')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=15, choices=(('Public', 'Public'), ('Private', 'Private')), default='Public')
    category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Invitation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_invitations')
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest_invitations')
    confirmation = models.BooleanField(default=False)
    date_invited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event.title} - {self.guest.username}"

class Contact(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_contacts')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_contacts')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user2}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="event_comments")
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)