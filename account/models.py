# -*- coding: UTF-8 -*-
# from django.db import models
from mongoengine import *
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Site(Document):
  # 訪客人次
	home_count = IntField(default=0)
	visitor_count = IntField(default=0)
	# 開站時間
	open_time = DateTimeField(auto_now_add=True)
	# 網站名稱
	site_name = StringField(max_length=50)
	# 網站圖片
	site_image =  StringField(max_length=255)

# 成員資料
class Org(Document):
    owner = ReferenceField('Profile')    

# 個人檔案資料
class Profile(Document):
    # user = OneToOneField(settings.AUTH_USER_MODEL, CASCADE, related_name="profile")
    user = ReferenceField('Org', reverse_delete_rule=CASCADE)
	# 使用者名稱
    username = StringField(max_length=50)  
	#user_id = IntField(default=0)
	# 積分：上傳作業
    work = IntField(default=0)
	# 積分：按讚
	# like = FloatField(default=0.0)
	# 積分：留言
	# reply = FloatField(default=0.0)
	# 大頭貼等級
    avatar = IntField(default=0)

    def __str__(self):
        return str(self.user.username)

Profile.register_delete_rule(Org, 'owner', DENY)
	
# 積分記錄 
class PointHistory(Document):
    # 使用者序號
	user_id = IntField(default=0)
	# 積分類別 
	kind = IntField(default=0)
	# 積分項目
	message = StringField(max_length=100)
	# 將積分項目超連結到某個頁面
	url = StringField(max_length=100)
	# 記載時間 
	publish = DateTimeField(default=timezone.now)

	def __unicode__(self):
		return str(self.user_id)
		
# 系統記錄
class Log(Document):
    # 使用者序號
    user_id = IntField(default=0)
		# 影片編號
    youtube_id = IntField(default=0)
    # 事件內容
    event = StringField(max_length=100)
	  # 發生時間 
    publish = DateTimeField(default=timezone.now)

    @property
    def user(self):
        return User.objects.get(id=self.user_id)
	
    def __unicode__(self):
        return str(self.user_id)+'--'+self.event

# 大廳訊息	
class Message(Document):
    author_id = IntField(default=0)
    reader_id = IntField(default=0)
    type = IntField(default=0)
    classroom_id = IntField(default=0)
    title = StringField(max_length=250)
    content = MultiLineStringField(default='')
    url = StringField(max_length=250)
    time = DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return self.title
		
    @classmethod
    def create(cls, title, url, time):
        message = cls(title=title, url=url, time=time)
        return message
			
class MessageContent(Document):
    message_id =  IntField(default=0)
    user_id = IntField(default=0)
    title =  StringField(max_length=250,null=True,blank=True)
    filename = StringField(max_length=250,null=True,blank=True)    
    publication_date = DateTimeField(default=timezone.now)

# 訊息    
class MessagePoll(Document):
    message_type = IntField(default=0)
    message_id = IntField(default=0)
    reader_id = IntField(default=0)
    classroom_id = IntField(default=0)
    read = BooleanField(default=False)
    
    @property
    def message(self):
        return Message.objects.get(id=self.message_id)
        
    @classmethod
    def create(cls, message_id, reader_id):
        messagepoll = cls(message_id=message_id, reader_id=reader_id)
        return messagepoll


class MessageFile(Document):
    message_id = IntField(default=0) 
    filename = MultiLineStringField()
    before_name = MultiLineStringField()
    upload_date = DateTimeField(default=timezone.now)
		
# 訪客 
class Visitor(Document):
    date = IntField(default=0)
    count = IntField(default=0)
    
# 訪客記錄
class VisitorLog(Document):
    visitor_id = IntField(default=0)    
    user_id = IntField(default=0)
    IP = StringField(max_length=20, default="")
    time = DateTimeField(auto_now_add=True)
    
# 學習領域
class Domain(Document):
	title = StringField(max_length=200, default="",verbose_name= '領域名稱')
	
# 年級
class Level(Document):
  title = StringField(max_length=200, default="",verbose_name= '年級')

# 家長
class Parent(Document):
  student_id = IntField(default=0)
  parent_id = IntField(default=0)
	
  class Meta:
      unique_together = ('student_id', 'parent_id',)		
			
#匯入
class ImportUser(Document):
	username = StringField(max_length=50, default="")
	first_name = StringField(max_length=50, default="")
	password = StringField(max_length=50, default="")
	email = StringField(max_length=100, default="")	
	