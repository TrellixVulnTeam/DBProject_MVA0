from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/', views.login , name='login'),
    url(r'^studentSignIn/', views.studentSignIn, name='studentSignIn'),
    url(r'^TeacherLogin/$', auth_views.login, name='login'),
    url(r'^TeacherLogout/$',auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^TeacherSignup/$', views.signup, name='signup'),
    url(r'^new_test/$', views.new_test, name='new_test'),
    url(r'^success/$', views.success, name='success'),
    url(r'^makeExam/$', views.makeexam, name='makeExam'),
    url(r'^makequestion/$', views.makequestion, name='newquestion'),
    url(r'^postNewExam/$', views.postNewExam, name='postNewExam'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^take_test/(?P<testName>.+?)/$', views.take_test, name='take_test'),
    url(r'^grade_test/(?P<testName>.+?)/$', views.grade_test, name='grade_test'),
    url(r'^delete_test/$', views.delete_test, name='delete_test'),
    url(r'^view_results/(?P<testName>.+?)/$', views.view_results, name='view_results'),

]