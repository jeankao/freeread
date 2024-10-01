from mongoengine import *
from django.contrib import admin
from .models import Annotation

admin.register(Annotation)
