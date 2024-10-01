# -*- coding: UTF-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from student.views import *
from student.views import GroupListView, ExamListView, TeamListView


urlpatterns = [
    # 選課
    path('classroom/enroll/<int:classroom_id>/',  login_required(views.classroom_enroll)),
    path('classroom/add/',  login_required(views.ClassroomAddListView.as_view())),
    path('classroom/<int:role>/',  login_required(views.ClassroomAddListView.as_view())),
    path('classroom/seat/<int:enroll_id>/<int:classroom_id>/',  login_required(views.seat_edit), name='seat_edit'),
    # 同學
    path('classmate/<int:classroom_id>/',  login_required(views.classmate)),
    path('loginlog/<int:user_id>/',  login_required(views.LoginLogListView.as_view())),
    #作業
    path('forum/<int:classroom_id>/<int:bookmark>/',  login_required(ForumListView.as_view()), name='work-list'),
    path('forum/submit/<int:classroom_id>/<int:index>/',  login_required(views.forum_submit)),
    path('forum/file_delete/',  login_required(views.forum_file_delete)),
    path('forum/memo/<int:classroom_id>/<int:index>/<int:action>/',  login_required(views.forum_memo)),
    path('forum/show/<int:index>/<int:user_id>/<int:classroom_id>/',  login_required(views.forum_show)),
    path('forum/history/<int:user_id>/<int:index>/<int:classroom_id>/',  login_required(views.forum_history)),
    path('forum/people/',  login_required(views.forum_people), name='people'),
    path('forum/guestbook/',  login_required(views.forum_guestbook), name='guestbook'),
    path('forum/score/',  login_required(views.forum_score), name='score'),
    path('forum/jieba/<int:classroom_id>/<int:index>/',  login_required(views.forum_jieba)),
    path('forum/word/<int:classroom_id>/<int:index>/<str:word>',  login_required(views.forum_word)),
    path('forum/download/<int:file_id>/',  login_required(views.forum_download), name='forum-download'),
    path('forum/showpic/<int:file_id>/',  login_required(views.forum_showpic), name='forum-showpic'),
    path('forum/publish/<int:classroom_id>/<int:index>/<int:action>/',  login_required(views.forum_publish), name='forum-publish'),
    #公告
    path('announce/<int:classroom_id>/',  login_required(AnnounceListView.as_view()), name='announce-list'),
    #組別
    path('group/<int:classroom_id>/',  login_required(GroupListView.as_view()), name='group-list'),
    path('group/list/<int:group_id>/',  login_required(views.group_list), name='group-list'),
    path('group/add/<int:group_id>/<int:number>/<int:enroll_id>',  login_required(views.group_join), name='group-join'),    
    path('group/leader/<int:group_id>/<int:number>/<int:enroll_id>/',  login_required(views.group_leader)),
    #思辨
    path('speculation/<int:classroom_id>/<int:bookmark>/',  login_required(SpeculationListView.as_view()), name='work-list'),
    path('speculation/submit/<int:classroom_id>/<int:index>/',  login_required(views.speculation_submit)),    
    path('speculation/publish/<int:classroom_id>/<int:index>/<int:action>/',  login_required(views.speculation_publish), name='speculation-publish'),
    path('speculation/annotate/<int:classroom_id>/<int:index>/<int:id>/',  login_required(SpeculationAnnotateView.as_view()), name='speculation-annotate'),
    path('speculation/annotateclass/<int:classroom_id>/<int:index>/<int:id>/',  login_required(SpeculationAnnotateClassView.as_view()), name='speculation-annotate-class'),    
    path('speculation/download/<int:file_id>/',  login_required(views.speculation_download), name='forum-download'),
    path('speculation/showpic/<int:file_id>/',  login_required(views.speculation_showpic), name='forum-showpic'),    
    path('speculation/score/',  login_required(views.speculation_score)),
	#測驗
    path('exam/<int:classroom_id>/',  login_required(ExamListView.as_view())),
    path('exam/question/<int:classroom_id>/<int:exam_id>/<int:examwork_id>/<int:question_id>/',  login_required(views.exam_question)),    
    path('exam/answer/',  login_required(views.exam_answer)),
    path('exam/submit/<int:classroom_id>/<int:exam_id>/<int:examwork_id>/',  login_required(views.exam_submit)),   
    path('exam/score/<int:classroom_id>/<int:exam_id>/<int:examwork_id>/<int:user_id>/<int:question_id>/',  login_required(views.exam_score)),
    path('video/log/',  login_required(views.video_log)),   
 	#合作
    path('team/<int:classroom_id>/',  login_required(TeamListView.as_view())),
    path('team/stage/<int:classroom_id>/<int:grouping>/<int:team_id>/',  login_required(views.team_stage)),   
    path('team/content/<int:classroom_id>/<int:grouping>/<int:team_id>/<int:ublish>/<int:stage>/',  login_required(TeamContentListView.as_view())),
    path('team/content/add/<int:classroom_id>/<int:grouping>/<int:team_id>/',  login_required(TeamContentCreateView.as_view())),   
    path('team/content/delete/<int:classroom_id>/<int:grouping>/<int:team_id>/<int:content_id>/',  login_required(views.team_delete)),
    path('team/content/edit/<int:classroom_id>/<int:grouping>/<int:team_id>/<int:content_id>/',  login_required(views.team_edit)),   
    path('team/publish/',  login_required(views.team_make_publish)),
    path('team/download/<int:file_id>/',  login_required(views.team_download), name='team-download'),   
    #課程
    path('course/<int:classroom_id>/',  login_required(CourseListView.as_view()), name='work-list'),
    path('course/content/<int:classroom_id>/<int:course_id>/',  login_required(CourseContentListView.as_view()), name='course-content'),   
    path('course/content/progress/',  login_required(views.course_progress)),
    path('course/status/<int:classroom_id>/<int:course_id>/',  login_required(CourseStatusListView.as_view())),   

]
