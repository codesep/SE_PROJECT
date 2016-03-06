from django.conf.urls import url

from . import views

app_name = 'GMS'
urlpatterns = [
           url(r'^$', views.home, name = 'home'),
           url(r'^adminPage/$', views.admin, name = 'adminPage'),
           url(r'^transcript/$', views.transcript, name = 'transcript'),
           url(r'^transcript/(?P<student_id>\w+)/$', views.transcript, name = 'transcript'),
           url(r'^login/$', views.login, name = 'login'),
           url(r'^logout/$', views.logout, name = 'logout'),
           url(r'^giveGrade/$', views.giveGrade, name = 'giveGrade'),
           url(r'^giveGrade/(?P<course_id>\w+)/$', views.giveGrade, name = 'giveGrade'),
           url(r'^addStudent/$', views.addStudent, name = 'addStudent'),
           url(r'^addInstructor/$', views.addInstructor, name = 'addInstructor'),
           url(r'^addCourse/$', views.addCourse, name = 'addCourse'),
           url(r'^saveStudent/$', views.saveStudent, name = 'saveStudent'),
           url(r'^registerStudent/$', views.registerStudent, name = 'registerStudent'),
           url(r'^successregisterStudent/$', views.successregisterStudent, name = 'successregisterStudent'),
           url(r'^successaddStudent/$', views.successaddStudent, name = 'successaddStudent'),
           url(r'^successaddInstructor/$', views.successaddInstructor, name = 'successaddInstructor'),
           url(r'^successaddCourse/$', views.successaddCourse, name = 'successaddCourse'),
           url(r'^saveRegisterStudent/$', views.saveRegisterStudent, name = 'saveRegisterStudent'),
           url(r'^saveCourse/$', views.saveCourse, name = 'saveCourse'),
           url(r'^saveInstructor/$', views.saveInstructor, name = 'saveInstructor')
]