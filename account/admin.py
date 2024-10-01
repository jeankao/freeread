from mongoengine import *
from django.contrib import admin
from account.models import Site, Profile, Log
# from account.models import Site, ImportUser, Log

# disconnect("default")
# connect("default")

admin.register(Site)
admin.register(Profile)
admin.register(Log)

# disconnect("default")
