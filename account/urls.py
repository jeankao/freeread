from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # post views
    path('dashboard/<int:action>/',  views.MessageListView.as_view()),
    #登入
    path('login/<int:role>/', views.user_login, name='login'),
    #註冊帳號
    path('register/', views.register),
    #註冊學校
    #path('register_school/', views.register_school),
    #登出
    path('logout/',auth_views.LogoutView.as_view()),
    #列出所有帳號
    path('userlist/<int:group>/', views.UserListView.as_view()),
    # 作者
    #path('author/', views.author),
    # 關於我們
    #path('about/', views.about),
    # 連絡我們
    #path('contact/', views.contact),
    # 教材研發
    #path('people/', views.people),
    # 數據統計
    #path('statics/lesson/', views.LessonCountView.as_view()),
    #訪客
    path('statics/login/', views.VisitorListView.as_view()),
    path('statics/login/log/<int:visitor_id>/', login_required(views.VisitorLogListView.as_view())),
    # 讀取訊息
    path('message/<int:messagepoll_id>/', login_required(views.message)),
    #個人檔案
    path('profile/<int:user_id>/', login_required(views.profile)),
    #修改密碼
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/<int:user_id>/', login_required(views.password)),
    #修改真實姓名
    path('realname/<int:user_id>/', login_required(views.adminrealname)),
    path('realname/', login_required(views.realname), name='realname'),
    #修改學校
    #path('school/', login_required(views.adminschool)),
    #修改信箱
    path('email/', login_required(views.adminemail)),
    #積分記錄
    path('log/<int:kind>/<int:user_id>/', views.LogListView.as_view()),
    #管理介面
    path('admin/', login_required(views.admin)),
    #path('admin/schools/', login_required(views.schools)),
    #path('admin/school/<int:pk>/', login_required(views.SchoolUpdateView.as_view())),
    #設定教師
    path('teacher/make/', login_required(views.make)),
    path('teacher/apply/', login_required(views.teacher_apply)),
    # 列所出有圖像
    path('avatar/', views.avatar),
    # 私訊
    path('line/', login_required(views.LineListView.as_view())),
    path('line/class/<int:classroom_id>/', login_required(views.LineClassListView.as_view())),
    path('line/add/<int:classroom_id>/<int:user_id>/', login_required(views.LineCreateView.as_view())),
    path('line/reply/<int:classroom_id>/<int:user_id>/<int:message_id>/', login_required(views.LineReplyView.as_view())),
    path('line/detail/<int:classroom_id>/<int:message_id>/', login_required(views.line_detail)),
	path('line/download/<int:file_id>/', views.line_download, name='forum-download'),
	path('line/showpic/<int:file_id>/', login_required(views.line_showpic), name='forum-showpic'),
    path('line/teacher/', login_required(views.LineTeacherCreateView.as_view())),
  
    #訪客
    path('visitor/', views.VisitorListView.as_view()),    
    path('visitorlog/<int:visitor_id>/', login_required(views.VisitorLogListView.as_view())),             
    

    #系統事件記錄
    path('event/<int:user_id>/', login_required(views.EventListView.as_view())),
    path('event/admin/', login_required(views.EventAdminListView.as_view())),
    path('event/admin/classroom/<int:classroom_id>/', login_required(views.EventAdminClassroomListView.as_view())),
    path('event/calendar/<int:user_id>/', login_required(views.EventCalendarView.as_view())),	  
    path('event/timeline/<int:user_id>/', login_required(views.EventTimeLineView.as_view())), 
    path('event/timelog/<int:user_id>/<int:hour>/', login_required(views.EventTimeLogView.as_view())),   
    path('event/video/<int:classroom_id>/', login_required(views.EventVideoView.as_view())),   
    #討論區作業
    path('forum/<int:user_id>/', login_required(views.ForumListView.as_view())),	 
    #思辨區作業
    path('speculation/<int:user_id>/', login_required(views.SpeculationListView.as_view())),	 	
    #設定家長
    path('parent/', login_required(views.ParentListView.as_view())),
    path('parent/search/', login_required(views.ParentSearchListView.as_view())),
    path('parent/child/', login_required(views.ParentChildListView.as_view())),  
    path('parent/make/', login_required(views.parent_make), name='parent_make'),      
	#大量匯入帳號
    path('import/upload/', login_required(views.import_sheet), name='import_upload'),   	
    path('import/user/', login_required(views.import_user), name='import_user'),   		
]
