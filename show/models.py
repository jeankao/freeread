# -*- coding: UTF-8 -*-
# from django.db import models
from mongoengine import *
from django.utils import timezone
from django.contrib.auth.models import User

class Round(Document):
    classroom_id = IntField(default=0)
    gourp_id = IntField(default=0)
    publish = DateTimeField(default=timezone.now)    

# 分組作品
class ShowGroup(Document):
    round_id = IntField(default=0)
    youtube = StringField(max_length=250)
    done = BooleanField(default=False)
    open =  BooleanField(default=False)
	
# 評分
class ShowReview(Document):
    show_id = IntField(default=0)
    student_id = IntField(default=0)
    score1 = IntField(default=0)
    score2 = IntField(default=0)
    score3 = IntField(default=0)
    comment = MultiLineStringField()
    publish = DateTimeField(default=timezone.now)
    done = BooleanField(default=False)	
	
    @property        
    def student(self):
        return User.objects.get(id=self.student_id)      