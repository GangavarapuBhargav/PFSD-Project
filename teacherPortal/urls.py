from django.urls import path
from . import views

urlpatterns = [
    path('timetable/',views.timetable,name='timetable'),
    path('onlineSessions', views.onlineSessions, name='onlineSessions'),
    path('assignments/',views.assignments, name='assignments'),
    path('schedule/',views.schedule,name='schedule'),
    
]

