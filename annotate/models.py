# -*- coding: UTF-8 -*-
# from django.db import models
from mongoengine import *
from django.contrib.auth.models import User
from teacher.models import Classroom
from django.utils import timezone
from django.http import JsonResponse
import json

class Annotation(Document):
  user_id     = IntField(default=0)
  # annotation: 由 annotatejs 產生的標註內容
  annotation  = MultiLineStringField(default='')
  # created: 建立時間
  created     = DateTimeField(default=timezone.now)
  # modified: 最後修改時間
  updated     = DateTimeField(default=timezone.now)
  # findex: 討論區id
  findex      = IntField(default=0)
  # ftype: 0: 討論區, 1: 思辨區
  ftype       = IntField(default=0)
  # mid: 思辨區素材id, 討論區此欄為 0
  mid         = IntField(default=0)
  # stu_id: 學生id
  stuid       = IntField(default=0)
  # atype: 標註類別(教師設定)
  atype       = IntField(default=0)
  
  def __unicode__(self):
    user = User.objects.filter(id=self.user_id)[0]
    annotation_obj = json.loads(self.annotation)    
    return user.first_name+" : "+annotation_obj["text"]