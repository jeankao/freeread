# -*- coding: UTF-8 -*-
# from django.db import models
from mongoengine import *
from django.contrib.auth.models import User
from teacher.models import Classroom
from django.utils import timezone
from django.http import JsonResponse
import json

# 學生選課資料
class Enroll(Document):
    # 學生序號
    student_id = IntField(default=0)
    # 班級序號
    classroom_id = IntField(default=0)
    # 座號
    seat = IntField(default=0)
    # 組別
    group = IntField(default=0)
    @property
	
    def classroom(self):
        return Classroom.objects.get(id=self.classroom_id)  

    @property        
    def student(self):
        return User.objects.get(id=self.student_id)      

    def __str__(self):
        return str(self.id)+":"+str(self.classroom_id)    

    class Meta:
        unique_together = ('student_id', 'classroom_id',)		
    
# 學生組別    
class EnrollGroup(Document):
    name = StringField(max_length=30)
    classroom_id = IntField(default=0)

#作業
class SFWork(Document):
    student_id = IntField(default=0)
    index = IntField()
    memo = MultiLineStringField(default='')
    memo_e =  IntField(default=0)
    memo_c = IntField(default=0)		
    publish = BooleanField(default=False)
    publication_date = DateTimeField(default=timezone.now)
    reply_date = DateTimeField(default=timezone.now)
    score = IntField(default=0)
    scorer = IntField(default=0)
    comment = MultiLineStringField(default='',null=True,blank=True)
    comment_publication_date = DateTimeField(default=timezone.now)		
    likes = MultiLineStringField(default='')
    like_count = IntField(default=0)	
    reply = IntField(default=0)
		
    def __unicode__(self):
        user = User.objects.filter(id=self.student_id)[0]
        index = self.index
        return user.first_name+"("+str(index)+")"

class SFContent(Document):
    index =  IntField(default=0)
    student_id = IntField(default=0)
    work_id = IntField(default=0)
    title =  StringField(max_length=250,null=True,blank=True)
    filename = StringField(max_length=60,null=True,blank=True)    
    publication_date = DateTimeField(default=timezone.now)
    delete_date = DateTimeField(default=timezone.now)		
    visible = BooleanField(default=True)

#討論留言
class SFReply(Document):
    index = IntField(default=0)
    work_id =  IntField(default=0)
    user_id = IntField(default=0)
    memo =  MultiLineStringField(default='')
    publication_date = DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.memo

		
#思辨文章
class SSpeculationWork(Document):
    student_id = IntField(default=0)
    index = IntField()
    memo = MultiLineStringField(default='')
    publish = BooleanField(default=False)
    publication_date = DateTimeField(default=timezone.now)
    reply_date = DateTimeField(default=timezone.now)
    score = IntField(default=0)
    scorer = IntField(default=0)
    comment = MultiLineStringField(default='',null=True,blank=True)
    comment_publication_date = DateTimeField(default=timezone.now)	
    likes = MultiLineStringField(default='')
    like_count = IntField(default=0)	
    reply = IntField(default=0)
		
    def __unicode__(self):
        user = User.objects.filter(id=self.student_id)[0]
        index = self.index
        return user.first_name+"("+str(index)+")"

class SSpeculationContent(Document):
    index =  IntField(default=0)
    student_id = IntField(default=0)
    work_id = IntField(default=0)
    title =  StringField(max_length=250,null=True,blank=True)
    filename = StringField(max_length=60,null=True,blank=True)    
    publication_date = DateTimeField(default=timezone.now)
    delete_date = DateTimeField(default=timezone.now)		
    visible = BooleanField(default=True)

class StudentGroup(Document):
    group_id = IntField(default=0)
    enroll_id = IntField(default=0)
    group = IntField(default=0)		

    class Meta:
        unique_together = ('enroll_id', 'group_id',)		

class StudentGroupLeader(Document):
    group_id = IntField(default=0)
    group = IntField(default=0)	
    enroll_id = IntField(default=0)	

    class Meta:
        unique_together = ('group_id', 'group')		        		

#測驗
class ExamWork(Document):
    student_id = IntField(default=0)
    exam_id = IntField()    
    questions = MultiLineStringField(default='')
    publish = BooleanField(default=False)
    publication_date = DateTimeField(default=timezone.now)
    score = IntField(default=0)
    scorer = IntField(default=0)
		
    def __unicode__(self):
        user = User.objects.filter(id=self.student_id)[0]
        exam_id = self.exam_id
        return user.first_name+"("+str(exam_id)+")"		
			
#測驗答案
class ExamAnswer(Document):
    examwork_id = IntField(default=0)
    question_id = IntField(default=0)
    student_id = IntField(default=0)
    answer = MultiLineStringField(default='')
    answer_right = BooleanField(default=False)
		
    class Meta:
        unique_together = ('student_id', 'examwork_id', 'question_id')		
		
class TeamContent(Document):
    team_id =  IntField(default=0)
    user_id = IntField(default=0)  
    types = IntField(default=0)
    title = StringField(max_length=250,null=True,blank=True)
    memo = MultiLineStringField(default='')
    link = StringField(max_length=250,null=True,blank=True)
    youtube = StringField(max_length=250,null=True,blank=True)
    youtube_length = IntField(default=0)
    file = FileField(blank=True,null=True)
    filename = StringField(max_length=60,null=True,blank=True)
    publication_date = DateTimeField(default=timezone.now)    
    publish = BooleanField(default=False)

class CourseContentProgress(Document):
    student_id = IntField(default=0)  
    content_id = IntField(default=0)  
    progress =IntField(default=0)  
    start_time = DateTimeField(default=timezone.now)    
    finish_time = DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('student_id', 'content_id')		    
      