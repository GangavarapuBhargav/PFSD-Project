from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyApp.urls')),
    path('teacherPortal/', include('teacherPortal.urls')),
    path('studentportal/', include('studentportal.urls')),
    path('course/',include('course.urls'))
]