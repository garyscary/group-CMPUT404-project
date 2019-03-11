from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import uuid

# from social_auth.signals import socialauth_registered

class Author(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    github = models.CharField(max_length=150, blank=False)
    displayName = models.CharField(max_length=150, blank=False)
    bio =  models.TextField(blank=True)
    host = models.URLField(blank=True)
    image = models.URLField(blank=True)
    feed = models.URLField(blank=True)
    localuser = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    friends = models.ManyToManyField("Author", blank=True, null=True, related_name="reverse_friends")

    def __str__(self):
        return "Author({},{},{})".format(self.displayName, self.localuser, self.github)

    def get_absolute_url(self):
        return reverse('test4', args=[str(self.github)])