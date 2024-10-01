from mongoengine import *
from django.contrib import admin
from student.models import *

admin.register(SFWork)
admin.register(Enroll)
admin.register(SFReply)
admin.register(StudentGroup)
admin.register(StudentGroupLeader)
admin.register(ExamWork)
admin.register(TeamContent)
