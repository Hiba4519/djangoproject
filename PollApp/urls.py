from django.urls import path
from . import views

app_name='PollApp'

urlpatterns=[
			path('',views.index,name='index'),
			path('register/',views.register,name='register'),
			path('login/',views.login,name='login'),
			path('login/home/<int:id>/',views.home,name='home'),
			path('home/<int:id>/',views.home,name='home'),
			path('home/<int:id>/createPoll/',views.createPoll,name='createPoll'),
			path('createPoll/<int:id>/home/',views.home,name='home'),
			path('home/<int:id>/createPoll/home/',views.home,name='home'),
			path('displayPoll/<int:id>/',views.displayPoll,name='displayPoll'),
			path('viewPoll/<int:id>/',views.viewPoll,name='viewPoll'),
			path('viewPoll/<int:id>/home/',views.home,name='home'),
			path('viewPoll/<int:id>/displayPoll/',views.displayPoll,name='displayPoll'),
			path('viewResult<int:id>/',views.viewResult,name='viewResult'),
			path('home/<int:id>/viewProfile/',views.viewProfile,name='viewProfile'),
			path('viewProfile/<int:id>/home/',views.home,name='home'),
			path('logout/',views.logout,name='logout'),
			]