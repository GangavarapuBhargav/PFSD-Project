from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'MyApp/index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            
            if len(user.username) == 4:
                return redirect('page1') 
            elif len(user.username) == 6:
                return redirect('teacherPortal')  
            elif len(user.username) >= 8:
                return redirect('studentPortal')
        else:
            return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'MyApp/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'MyApp/register.html', {'form': form})



def languages(request):
    return render(request, 'MyApp/languages.html')



def page1(request):
    return render(request, 'MyApp/page1.html')


def page2(request):
    return render(request, 'MyApp/page2.html')


def page3(request):
    return render(request, 'MyApp/page3.html')


def page4(request):
    return render(request, 'MyApp/page4.html')


def page5(request):
    return render(request, 'MyApp/page5.html')


def page6(request):
    return render(request, 'MyApp/page6.html')


def page7(request):
    return render(request, 'MyApp/page7.html')


def page8(request):
    return render(request, 'MyApp/page8.html')


def page9(request):
    return render(request, 'MyApp/page9.html')


def page10(request):
    return render(request, 'MyApp/page10.html')


def page11(request):
    return render(request, 'MyApp/page11.html')


def page12(request):
    return render(request, 'MyApp/page12.html')


def page12(request):
    return render(request, 'MyApp/page12.html')


def page13(request):
    return render(request, 'MyApp/page13.html')

@login_required
def page14(request):
    return render(request, 'MyApp/page14.html')

@login_required
def page15(request):
    return render(request, 'MyApp/page15.html')

@login_required
def page16(request):
    return render(request, 'MyApp/page16.html')


@login_required
def page17(request):
    return render(request, 'MyApp/page17.html')


@login_required
def page18(request):
    return render(request, 'MyApp/page18.html')








def quiz(request):
    return render(request, 'MyApp/quiz.html')

def teacherPortal(request):
    return render(request, 'MyApp/teacherPortal.html')

def studentPortal(request):
    return render(request,'MyApp/studentPortal.html')



