# -*- coding: UTF-8 -*-
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from teacher.views import *

urlpatterns = [

    path('member/',  login_required(views.TeacherListView.as_view())),  
    path('student/<int:teacher_id>/',  login_required(views.StudentListView.as_view())),  

    # 班級
    path('classroom/',  login_required(views.ClassroomListView.as_view())),  
    path('classroom/add/',  login_required(views.ClassroomCreateView.as_view())), 
    path('classroom/edit/<int:classroom_id>/',  login_required(views.classroom_edit)),  
    path('classroom/assistant/<int:classroom_id>/',  login_required(views.classroom_assistant)), 
    path('classroom/assistant/add/<int:classroom_id>/',  login_required(views.AssistantListView.as_view())),  

    # 分組
    path('group/<int:classroom_id>/',  login_required(views.GroupListView.as_view())), 
    path('group/add/<int:classroom_id>/',  login_required(views.GroupCreateView.as_view())),  
    path('group/edit/<int:classroom_id>/<int:pk>/',  login_required(views.GroupUpdateView.as_view())), 
    path('group/make/',  login_required(views.make)), 
    path('group/make2/<int:group_id>/<int:action>/',  login_required(views.make2)),  

    # 設定助教
    path('assistant/',  login_required(views.AssistantClassroomListView.as_view())), 
    path('assistant/make/',  login_required(views.assistant_make), name='make'), 

    # 退選    
    path('unenroll/<int:enroll_id>/<int:classroom_id>/',  login_required(views.unenroll)),  

    # 討論區
    path('forum/<int:categroy>/<int:categroy_id>/',  login_required(ForumAllListView.as_view()), name='forum-all'), 
    path('forum/show/<int:forum_id>/',  login_required(views.forum_show), name='forum-show'), 
    path('forum/edit/<int:classroom_id>/<int:pk>/',  login_required(ForumEditUpdateView.as_view()), name='forum-edit'),    
    path('forum/<int:classroom_id>/',  login_required(ForumListView.as_view()), name='forum-list'), 
    path('forum/add/<int:classroom_id>/<int:forum_id>/',  login_required(ForumCreateView.as_view()), name='forum-add'), 
    path('forum/category/<int:classroom_id>/<int:forum_id>/',  login_required(views.forum_categroy), name='forum-category'),    
    path('forum/deadline/<int:classroom_id>/<int:forum_id>/',  login_required(views.forum_deadline), name='forum-deadline'), 
    path('forum/deadline/set/',  login_required(views.forum_deadline_set), name='forum-deatline-set'), 
    path('forum/deadline/date/',  login_required(views.forum_deadline_date), name='forum-category'),    
    path('forum/deadline/<int:classroom_id>/<int:forum_id>/',  login_required(views.forum_deadline)), 
    path('forum/download/<int:content_id>/',  login_required(views.forum_download), name='forum-download'), 
    path('forum/content/<int:forum_id>/',  login_required(ForumContentListView.as_view()), name='forum-content'),    
    path('forum/content/add/<int:forum_id>/',  login_required(ForumContentCreateView.as_view()), name='forum-content-add'), 
    path('forum/content/delete/<int:forum_id>/<int:content_id>/',  login_required(views.forum_delete), name='forum-content-delete'), 
    path('forum/content/edit/<int:forum_id>/<int:content_id>/',  login_required(views.forum_edit), name='forum-content-edit'),    
    path('forum/class/<int:forum_id>/',  login_required(ForumClassListView.as_view()), name='forum-class'), 
    path('forum/export/<int:classroom_id>/<int:forum_id>/',  login_required(views.forum_export), name='forum-export'), 
    path('forum/grade/<int:classroom_id>/<int:action>/',  login_required(views.forum_grade), name='forum-grade'),        
    # 設定班級
    path('forum/class/switch/',  login_required(views.forum_switch), name='make'),    

    # 公告
    path('announce/add/<int:classroom_id>/',  login_required(AnnounceCreateView.as_view()), name='announce-add'), 
    
    # 思辨區    
    path('speculation/<int:categroy>/<int:categroy_id>/',  login_required(SpeculationAllListView.as_view()), name='forum-all'), 
    path('speculation/show/<int:forum_id>/',  login_required(views.speculation_show), name='forum-show'),    
    path('speculation/edit/<int:classroom_id>/<int:pk>/',  login_required(SpeculationEditUpdateView.as_view()), name='forum-edit'), 
    path('speculation/<int:classroom_id>/',  login_required(SpeculationListView.as_view()), name='forum-list'), 
    path('speculation/add/<int:classroom_id>/',  login_required(SpeculationCreateView.as_view()), name='forum-add'),
    path('speculation/category/<int:classroom_id>/<int:forum_id>/',  login_required(views.speculation_categroy), name='forum-category'), 
    path('speculation/deadline/<int:classroom_id>/<int:forum_id>/',  login_required(views.speculation_deadline), name='forum-deadline'),    
    path('speculation/deadline/set/',  login_required(views.speculation_deadline_set), name='forum-deatline-set'), 
    path('speculation/deadline/date/',  login_required(views.speculation_deadline_date), name='forum-deatline-date'), 
    path('speculation/deadline/<int:classroom_id>/<int:forum_id>/',  login_required(views.speculation_deadline), name='forum-category'),
    path('speculation/download/<int:content_id>/',  login_required(views.speculation_download), name='forum-download'), 
    path('speculation/content/<int:forum_id>/',  login_required(SpeculationContentListView.as_view()), name='forum-content'),    
    path('speculation/content/add/<int:forum_id>/',  login_required(SpeculationContentCreateView.as_view()), name='forum-content-add'), 
    path('speculation/content/delete/<int:forum_id>/<int:content_id>/',  login_required(views.speculation_delete), name='forum-content-delete'), 
    path('speculation/content/edit/<int:forum_id>/<int:content_id>/',  login_required(views.speculation_edit), name='forum-content-edit'),
    path('speculation/class/<int:forum_id>/',  login_required(SpeculationClassListView.as_view()), name='forum-class'), 
    path('speculation/export/<int:classroom_id>/<int:forum_id>/',  login_required(views.speculation_export), name='forum-export'),
    path('speculation/grade/<int:classroom_id>/<int:action>/',  login_required(views.speculation_grade)), 

    # 設定班級
    path('speculation/class/switch/',  login_required(views.speculation_switch), name='make'), 
    
    # 設定分組
    path('speculation/group/<int:classroom_id>/<int:forum_id>/',  login_required(views.speculation_group), name='group'),
    path('speculation/group/set/',  login_required(views.speculation_group_set), name='group'),

    # 文字註記    
    path('speculation/annotation/<int:forum_id>/',  login_required(SpeculationAnnotationListView.as_view()), name='make'), 
    path('speculation/annotation/add/<int:forum_id>/',  login_required(SpeculationAnnotationCreateView.as_view()), name='forum-content-add'),  
    path('speculation/annotation/delete/<int:forum_id>/<int:content_id>/',  login_required(views.speculation_annotation_delete), name='forum-content-delete'), 
    path('speculation/annotation/edit/<int:forum_id>/<int:content_id>/',  login_required(views.speculation_annotation_edit), name='forum-content-edit'),   

    # 測驗區
    path('exam<int:categroy>/<int:categroy_id>/',  login_required(ExamAllListView.as_view())), 
    path('exam/<int:classroom_id>/',  login_required(ExamListView.as_view())), 
    path('exam/add/<int:classroom_id>/',  login_required(ExamCreateView.as_view())),
    path('exam/edit/<int:classroom_id>/<int:pk>/',  login_required(ExamEditUpdateView.as_view())), 
    path('exam/category/<int:classroom_id>/<int:exam_id>/',  login_required(views.exam_categroy)), 
    path('exam/class/<int:exam_id>/',  login_required(ExamClassListView.as_view())),
    path('exam/class/switch/',  login_required(views.exam_switch)), 
    path('exam/deadline/<int:classroom_id>/<int:exam_id>/',  login_required(views.exam_deadline)), 
    path('exam/deadline/set/',  login_required(views.exam_deadline_set)),
    path('exam/deadline/date/',  login_required(views.exam_deadline_date)), 
    path('exam/round/<int:classroom_id>/<int:exam_id>/',  login_required(views.exam_round)), 
    # path('exam/round/<int:>/',  login_required(views.)),
    path('exam/set/',  login_required(views.exam_round_set)), 
    path('exam/question/<int:exam_id>/',  login_required(ExamQuestionListView.as_view())), 
    path('exam/question/add/<int:exam_id>/',  login_required(ExamQuestionCreateView.as_view())),     
    path('exam/question/delete/<int:exam_id>/<int:question_id>/',  login_required(views.exam_question_delete)),
    path('exam/question/edit/<int:exam_id>/<int:question_id>/',  login_required(views.exam_question_edit)), 
    path('exam/publish/<int:exam_id>/<int:question_id>/',  login_required(views.exam_publish)), 
    path('exam/check/<int:exam_id>/',  login_required(views.exam_check)),  
    path('exam/check/make/',  login_required(views.exam_check_make)),
    path('exam/score/<int:classroom_id>/<int:exam_id>/',  login_required(views.exam_score)), 
    path('exam/excel/<int:classroom_id>/<int:exam_id>/',  login_required(views.exam_excel)), 

	  # 大量匯入選擇題    
    path('exam/import/upload/<int:types>/<int:exam_id>/',  login_required(views.exam_import_sheet)),  
    path('exam/import/question/<int:types>/<int:exam_id>/',  login_required(views.exam_import_question)),

    # 合作區    
    path('team/edit/<int:classroom_id>/<int:pk>/',  login_required(TeamEditUpdateView.as_view())),  
    path('team/<int:classroom_id>/',  login_required(TeamListView.as_view())),  
    path('team/add/<int:classroom_id>/',  login_required(TeamCreateView.as_view())),
    path('team/category/<int:classroom_id>/<int:team_id>/',  login_required(views.team_categroy)), 
    path('team/deadline/<int:classroom_id>/<int:team_id>/',  login_required(views.team_deadline)),  
    path('team/deadline/set/',  login_required(views.team_deadline_set)),  
    path('team/deadline/date/',  login_required(views.team_deadline_date)),
    path('team/deadline/<int:classroom_id>/<int:team_id>/',  login_required(views.team_deadline)), 
    path('team/class/<int:classroom_id>/<int:team_id>/',  login_required(views.team_class)),  
    path('team/class/<int:team_id>/',  login_required(TeamClassListView.as_view())),  
    path('team/class/switch/',  login_required(views.team_switch)),
    path('team/group/<int:classroom_id>/<int:team_id>/',  login_required(views.team_group)), 
    path('team/group/set/',  login_required(views.team_group_set)), 

	  # 影片觀看記錄    
    path('video/<int:classroom_id>/<int:forum_id>/<int:work_id>/',  login_required(views.EventVideoView.as_view())), 
    path('video/length/',  login_required(views.video_length)),  
    path('video/user/<int:classroom_id>/<int:content_id>/<int:user_id>/',  login_required(VideoListView.as_view())),

    # 課程區
    path('course/<int:categroy>/<int:categroy_id>/',  login_required(CourseAllListView.as_view()), name='course-all'), 
    path('course/edit/<int:classroom_id>/<int:pk>/',  login_required(CourseEditUpdateView.as_view()), name='course-edit'), 
    path('course/<int:classroom_id>/',  login_required(CourseListView.as_view()), name='course-list'), 
    path('course/add/<int:classroom_id>/',  login_required(CourseCreateView.as_view()), name='course-add'),
    path('course/category/<int:classroom_id>/<int:course_id>/',  login_required(views.course_categroy), name='course-category'), 
    path('course/deadline<int:classroom_id>/<int:course_id>/',  login_required(views.course_deadline), name='course-deadline'), 
    path('course/deadline/set/',  login_required(views.course_deadline_set), name='course-deatline-set'), 
    path('course/deadline/date/',  login_required(views.course_deadline_date), name='course-deatline-date'), 
    path('course/deadline/<int:classroom_id>/<int:course_id>/',  login_required(views.course_deadline), name='course-category'), 
    path('course/download/<int:classroom_id>/<int:content_id>/',  login_required(views.course_download), name='course-download'), 
    path('course/content/<int:classroom_id>/<int:course_id>/',  login_required(CourseContentListView.as_view()), name='course-content'), 
    path('course/content/add/<int:classroom_id>/<int:course_id>/',  login_required(CourseContentCreateView.as_view()), name='course-content-add'),   
    path('course/content/delete/<int:classroom_id>/<int:course_id>/<int:content_id>/',  login_required(views.course_delete), name='course-content-delete'), 
    path('course/content/edit/<int:classroom_id>/<int:course_id>/<int:content_id>/',  login_required(views.course_edit), name='course-content-edit'), 
    path('course/class/<int:course_id>/',  login_required(CourseClassListView.as_view()), name='course-class'), 
    path('course/class/switch/',  login_required(views.course_switch)), 
    path('course/exercise/<int:classroom_id>/<int:content_id>/',  login_required(CourseExerciseListView.as_view()), name='course-excise'), 
    path('course/exercise/add/<int:classroom_id>/<int:content_id>/<int:types>/',  login_required(CourseExerciseAddListView.as_view()), name='course-excise'),
    path('course/group/<int:classroom_id>/<int:course_id>/',  login_required(views.course_group)), 
    path('course/group/set/',  login_required(views.course_group_set)),
    path('course/exercise/make/',  login_required(views.exercise_make)),   
]
