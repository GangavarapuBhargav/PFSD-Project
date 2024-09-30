from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('course1/', views.course1, name='course1'),
    path('course2/', views.course2, name='course2'),
    path('course3/', views.course3, name='course3'),
    path('course4/', views.course4, name='course4'),
    path('course5/', views.course5, name='course5'),
    path('course6/', views.course6, name='course6'),
    path('course7/', views.course7, name='course7'),
    path('course8/', views.course8, name='course8'),
    path('course9/', views.course9, name='course9'),
    path('course10/', views.course10, name='course10'),
    path('course11/', views.course11, name='course11'),
    path('course12/', views.course12, name='course12'),
    path('course13/', views.course13, name='course13'),
    path('course14/', views.course14, name='course14'),
    path('course15/', views.course15, name='course15'),
    path('course16/', views.course16, name='course16'),
    path('course17/', views.course17, name='course17'),
    path('course18/', views.course18, name='course18'),
    path('quiz1/', views.quiz1, name='quiz1'),
]
