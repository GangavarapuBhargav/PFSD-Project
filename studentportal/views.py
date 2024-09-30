from django.shortcuts import render,redirect

# Create your views here.
def student_assignments(request):
    return render(request,'studentportal/student_assignments.html')

def courses(request):
    return render(request,'courses.html')

def studentTimetable(request):
    return render(request,'studentportal/studentTimetable.html')