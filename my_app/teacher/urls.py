
from . import views
from django.urls import path
from teacher.views import index, login, logout,register, sendmail,teacher

app_name = 'teacher'
urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('register', register, name="register"),
    path('logout/', logout, name='logout'),
    path('teacher/', teacher, name='teacher'),
    path('sendmail/', sendmail, name='sendmail'),
]