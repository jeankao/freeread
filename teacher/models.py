# -*- coding: UTF-8 -*-
# from django.db import models
from mongoengine import *
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# 班級
class Classroom(Document):
    # 班級名稱
    name = StringField(max_length=30)
    # 選課密碼
    password = StringField(max_length=30)
    # 授課教師
    teacher_id = IntField(default=0)
    # 學習領域
    domains = MultiLineStringField(default='')
    #年級
    levels = MultiLineStringField(default='')

    @property
    def teacher(self):
        return User.objects.get(id=self.teacher_id)

    def __unicode__(self):
        return self.name

#班級助教
class Assistant(Document):
    classroom_id = IntField(default=0)
    user_id = IntField(default=0)

#討論區
class FWork(Document):
    title = StringField(max_length=250,verbose_name= '討論主題')
    teacher_id = IntField(default=0)
    classroom_id = IntField(default=0)
    time = DateTimeField(default=timezone.now)
    domains = MultiLineStringField(default='')
    levels = MultiLineStringField(default='')

def get_deadline():
    return timezone.now() + timedelta(days=14)

class FClass(Document):
    forum_id = IntField(default=0)
    classroom_id =  IntField(default=0)
    publication_date = DateTimeField(default=timezone.now)
    deadline = BooleanField(default=False)
    deadline_date = DateTimeField(default=get_deadline)

    def __unicode__(self):
        return str(self.forum_id)

class FContent(Document):
    forum_id =  IntField(default=0)
    types = IntField(default=0)
    title = StringField(max_length=250,null=True,blank=True)
    memo = MultiLineStringField(default='')
    link = StringField(max_length=250,null=True,blank=True)
    youtube = StringField(max_length=250,null=True,blank=True)
    youtube_length = IntField(default=0)
    file = FileField(blank=True,null=True)
    filename = StringField(max_length=60,null=True,blank=True)

#思辨區
class SpeculationWork(Document):
    title = StringField(max_length=250,verbose_name= '思辨主題')
    teacher_id = IntField(default=0)
    classroom_id = IntField(default=0)
    time = DateTimeField(default=timezone.now)
    domains = MultiLineStringField(default='')
    levels = MultiLineStringField(default='')

class SpeculationClass(Document):
    forum_id = IntField(default=0)
    classroom_id =  IntField(default=0)
    publication_date = DateTimeField(default=timezone.now)
    deadline = BooleanField(default=False)
    deadline_date = DateTimeField(default=get_deadline)
    group =  IntField(default=0)

    def __unicode__(self):
        return str(self.forum_id)

class SpeculationContent(Document):
    forum_id =  IntField(default=0)
    types = IntField(default=0)
    title = StringField(max_length=250,null=True,blank=True)
    memo = MultiLineStringField(default='')
    text = MultiLineStringField(default='')
    link = StringField(max_length=250,null=True,blank=True)
    youtube = StringField(max_length=250,null=True,blank=True)
    file = FileField(blank=True,null=True)
    filename = StringField(max_length=60,null=True,blank=True)

class SpeculationAnnotation(Document):
    forum_id =  IntField(default=0)
    kind = StringField(max_length=250,null=True,blank=True)
    color = StringField(max_length=7,null=True,blank=True)

class ClassroomGroup(Document):
    # 班級
    classroom_id = IntField(default=0)
    #分組名稱
    title = StringField(max_length=250,null=True,blank=True)
    #小組數目
    numbers = IntField(default=6)
    #開放分組
    opening = BooleanField(default=True)
    #分組方式
    assign = IntField(default=0)

    def __unicode__(self):
        return self.classroom_id

#測驗
class Exam(Document):
    title = StringField(max_length=250,verbose_name= '測驗主題')
    user_id = IntField(default=0)
    classroom_id = IntField(default=0)
    time = DateTimeField(default=timezone.now)
    domains = MultiLineStringField(default='')
    levels = MultiLineStringField(default='')
    opening = BooleanField(default=False)


class ExamClass(Document):
    exam_id = IntField(default=0)
    classroom_id =  IntField(default=0)
    publication_date = DateTimeField(default=timezone.now)
    deadline = BooleanField(default=False)
    deadline_date = DateTimeField(default=get_deadline)
    round_limit = IntField(default=1)

    def __unicode__(self):
        return str(self.exam_id)

    class Meta:
        unique_together = ('exam_id', 'classroom_id',)

class ExamQuestion(Document):
    exam_id = IntField(default=0)
    types = IntField(default=0)
    #題目敘述
    title = MultiLineStringField(default='')
    title_pic = FileField(blank=True,null=True)
    title_filename = StringField(max_length=60,null=True,blank=True)    
    #選擇題選項
    option1 = StringField(max_length=250,null=True,blank=True)
    option2 = StringField(max_length=250,null=True,blank=True)
    option3 = StringField(max_length=250,null=True,blank=True)
    option4 = StringField(max_length=250,null=True,blank=True) 
    #簡答題
    answer = MultiLineStringField(default='')
    #配分 
    score = IntField(default=0)

class ExamImportQuestion(Document):
    title = MultiLineStringField(default='')
    option1 = StringField(max_length=250,null=True,blank=True)
    option2 = StringField(max_length=250,null=True,blank=True)
    option3 = StringField(max_length=250,null=True,blank=True)
    option4 = StringField(max_length=250,null=True,blank=True)
    answer= MultiLineStringField(default='')
    score = IntField(default=0)    

#合作區
class TeamWork(Document):
    title = StringField(max_length=250,verbose_name= '任務主題')
    teacher_id = IntField(default=0)
    classroom_id = IntField(default=0)
    time = DateTimeField(default=timezone.now)
    domains = MultiLineStringField(default='')
    levels = MultiLineStringField(default='')

class TeamClass(Document):
    team_id = IntField(default=0)
    classroom_id =  IntField(default=0)
    group =  IntField(default=0)
    publication_date = DateTimeField(default=timezone.now)
    deadline = BooleanField(default=False)
    deadline_date = DateTimeField(default=get_deadline)

    def __unicode__(self):
        return str(self.team_id)

    class Meta:
        unique_together = ('team_id', 'classroom_id',)

class TeamContent(Document):
    team_id =  IntField(default=0)
    types = IntField(default=0)
    title = StringField(max_length=250,null=True,blank=True)
    memo = MultiLineStringField(default='')
    link = StringField(max_length=250,null=True,blank=True)
    youtube = StringField(max_length=250,null=True,blank=True)
    file = FileField(blank=True,null=True)
    filename = StringField(max_length=60,null=True,blank=True)

#課程區
class CourseWork(Document):
    title = StringField(max_length=250,verbose_name= '課程主題')
    teacher_id = IntField(default=0)
    classroom_id = IntField(default=0)
    time = DateTimeField(default=timezone.now)
    domains = MultiLineStringField(default='')
    levels = MultiLineStringField(default='')

class CourseClass(Document):
    course_id = IntField(default=0)
    classroom_id =  IntField(default=0)
    group =  IntField(default=0)    
    publication_date = DateTimeField(default=timezone.now)
    deadline = BooleanField(default=False)
    deadline_date = DateTimeField(default=get_deadline)

    def __unicode__(self):
        return str(self.forum_id)

class CourseContent(Document):
    course_id =  IntField(default=0)
    types = IntField(default=0)
    title = StringField(max_length=250,null=True,blank=True)
    memo = MultiLineStringField(default='')
    link = StringField(max_length=250,null=True,blank=True)
    youtube = StringField(max_length=250,null=True,blank=True)
    youtube_length = IntField(default=0)
    file = FileField(blank=True,null=True)
    filename = StringField(max_length=60,null=True,blank=True)

class CourseExercise(Document):
    content_id =  IntField(default=0)
    types = IntField(default=0)
    exercise_id = IntField(default=0)

