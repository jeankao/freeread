from mongoengine import *
from django.contrib import admin
from teacher.models import FClass, FWork, SpeculationWork, SpeculationClass, ExamQuestion, CourseExercise


admin.register(FClass)

admin.register(FWork)

admin.register(SpeculationWork)

admin.register(SpeculationClass)

admin.register(ExamQuestion)

admin.register(CourseExercise)