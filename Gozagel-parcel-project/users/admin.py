from django.contrib import admin

# from .models import Profile, Addresses

# # Register your models here.

from users.models import Contacts
# Register your models here.
admin.site.register(Contacts)
