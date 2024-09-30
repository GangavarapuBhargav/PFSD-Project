from django.shortcuts import render, redirect

# Create your views here.

def timetable(request):
    return render(request,'teacherPortal/timetable.html')

def onlineSessions(request):
    return render(request,'teacherPortal/onlineSessions.html')

def assignments(request):
    return render(request,'teacherportal/assignments.html')

def schedule(request):
    return render(request,'teacherPortal/schedule.html')