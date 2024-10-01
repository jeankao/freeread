# -*- coding: UTF-8 -*-
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

  path('',  views.root ),  
  path('annotations/', login_required(views.root)),  
  path('annotations/', login_required(views.annotations)),  
  path('annotations/<int:annotation_id>/', login_required(views.single_annotation)),  
  path('search/', login_required(views.search)),  
]
