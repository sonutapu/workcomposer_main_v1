from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),

    path('index/',views.index,name='index'),
    path('components/',views.components,name='components'),
    path('forms/',views.forms,name='forms'),
    path('tables/',views.tables,name='tables'),
    path('notifications/',views.notifications,name='notifications'),
    path('typography/',views.typography,name='typography'),
    # path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('settingprofile/',views.settingprofile,name='settingprofile'),
    # path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('screen_capture/',views.screen_capture,name='screen_capture'),


    
   
    
    path('signup/', views.signup, name='signup'),
    # path('home/', views.home, name='home'),
    path('appusage/', views.appusage, name='appusage'),
    # path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('Userdetails/', views.Userdetails, name='Userdetails'),
    path('passwordchange/', views.passwordchange, name='passwordchange'),
    path('SendInvitation/', views.SendInvitation, name='SendInvitation'),
    path('AddNewUser/', views.AddNewUser, name='AddNewUser'),
    path('AddUserType/', views.AddUserType, name='AddUserType'),
    path('User/', views.User, name='User'),
    path('attendancezzzzzz/', views.attendance, name='attendance'),
    path('productivity/', views.productivity, name='productivity'),
    path('screenshots/', views.screenshots, name='screenshots'),
    path('editdata/<int:id>', views.editdata, name='editdata'),
    path('updatedata/<int:id>', views.updatedata, name='updatedata'),
    path('delete/<int:id>', views.deletedata, name='deletedata'),



    path('success',views.success,name='success'),
    path('createteam/',views.createteam,name='createteam'),
    path('deleteteam/<int:id>', views.deleteteam, name='deleteteam'),
    path('editteam/<int:id>', views.editteam, name='editteam'),
    path('updateteam/<int:id>',views.updateteam, name='updateteam'),
    path('createproject/', views.createproject, name='createproject'),
]