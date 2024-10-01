# -*- coding: UTF-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from teacher.views import *
from student.models import *
from account.models import *


urlpatterns = [
    # post views
    path('detail/<int:show_id>/',  login_required(ReviewUpdateView.as_view())), 
    path('score/<int:show_id>/',  login_required(ReviewListView.as_view())),  
    path('rank/<int:rank_id>/<int:round_id>/',  login_required(RankListView.as_view())),
    path('teacher/<int:classroom_id>/',  login_required(views.commentall)),  
    path('teacher/comment/<int:round_id>/<int:user_id>/',  login_required(views.classroom)),
    path('teacher/comment/<int:round_id>/',  login_required(TeacherListView.as_view())),  
    path('teacher/grading/<int:round_id>/',  login_required(TeacherListView.as_view())),
    path('teacher/scoring/<int:round_id>/',  login_required(ScoreListView.as_view())),  
   
]

