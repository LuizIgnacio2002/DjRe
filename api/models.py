from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True) # null=True means that it can be null, blank=True means that it can be blank
    updated = models.DateTimeField(auto_now=True) # auto_now=True means that it will update the time every time it is updated
    created = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that it will add the time when it is created

    def __str__(self):
        return self.body[:50] # this will return the first 50 characters of the body