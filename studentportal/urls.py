from django.urls import path
from . import views

urlpatterns = [
  path('student_assignments/',views.student_assignments, name='student_assignments'),
  path('courses/',views.courses, name='courses'),
  path('studentTimetable/',views.studentTimetable,name='studentTimetable'),
  path('student_schedule/',views.student_schedule,name='student_schedule'),
  

]