from django.contrib import admin

# Register your models here.

from .models import Note

admin.site.register(Note) # this will register the Note model in the admin page