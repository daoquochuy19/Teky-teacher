
from email import message
import email
import json
from multiprocessing import AuthenticationError, context
from re import template
from telnetlib import LOGOUT
from unittest import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from re import template
from django.shortcuts import redirect, render
from django.template import loader
from django.views import View
from django.contrib.auth import authenticate
from teacher.forms import LoginForm
from .models import AboutUs, AboutUs2, ActivitiesCultural, ActivitiesCultural2, BecomeLecturers, Partners, Partners2, RegisterTeacher, Teacher, TutorBlock, TutorBlock2, TutorIcon, TutorIcon2, WhyMakeTeacher, WhyMakeTeacher2
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserRegistrationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from email.message import EmailMessage

@login_required
def index(request):
    


    myBecomeLecturers=BecomeLecturers.objects.all().values()
    myTutorBlock=TutorBlock.objects.all().values()
    myTutorBlock2=TutorBlock2.objects.all().values()
    myTutorIcon=TutorIcon.objects.all().values()
    myTutorIcon2=TutorIcon2.objects.all().values()
    myWhyMakeTeacher=WhyMakeTeacher.objects.all().values()
    myWhyMakeTeacher2=WhyMakeTeacher2.objects.all().values()
    myActivitiesCultural=ActivitiesCultural.objects.all().values()
    myActivitiesCultural2=ActivitiesCultural2.objects.all().values()
    myAboutUs=AboutUs.objects.all().values()
    myAboutUs2=AboutUs2.objects.all().values()
    myRegisterTeacher=RegisterTeacher.objects.all().values()
    myPartners=Partners.objects.all().values()
    myPartners2=Partners2.objects.all().values()
    template = loader.get_template('index.html')
    context= {
        'myBecomeLecturers':myBecomeLecturers,
        'myTutorBlock':myTutorBlock,
        'myTutorBlock2':myTutorBlock2,
        'myTutorIcon':myTutorIcon,
        'myTutorIcon2':myTutorIcon2,
        'myWhyMakeTeacher':myWhyMakeTeacher,
        'myWhyMakeTeacher2':myWhyMakeTeacher2,
        'myActivitiesCultural':myActivitiesCultural,
        'myActivitiesCultural2':myActivitiesCultural2,
        'myAboutUs2':myAboutUs2,
        'myAboutUs':myAboutUs,
        'myRegisterTeacher':myRegisterTeacher,
        'myPartners':myPartners,
        'myPartners2':myPartners2,
    }
    return HttpResponse(template.render(context, request))
    
def sendmail(request):
    if request.method == 'POST':
        sender_email = request.POST['email']

        mail = EmailMessage(
            'This is title',
            'Cảm ơn bạn đã liên hệ với chúng tôi. Chúng tôi sẽ thông báo tới bạn khi có thông tin mới nhất về Teky!!!',
            settings.EMAIL_HOST_USER,
            [sender_email]
        )
        mail.fail_silently = True
        mail.send()
        messages.success(request, "Đăng ký thành công")
    return render(request, 'index.html', {})


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method=="POST":
        user_name = request.POST['username']
        matkhau = request.POST['password']
        my_user = authenticate(username=user_name, password=matkhau)
        if my_user is not None:
            auth_login(request, my_user)
            return HttpResponseRedirect('/') 
        else:
            messages.success(request, ("Incorrect account or password"))
            return redirect('login')
    return render(request, 'login.html', context={'form':LoginForm()})    

    




def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)    
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
        else:           
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = UserRegistrationForm()
    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )
    


def logout(request):    
    auth.logout(request)
    return HttpResponseRedirect('/')


def teacher(request):
    if request.method=="POST":
        name=request.POST['name']
        number_phone=request.POST['number_phone']
        email=request.POST['email']
        cv=request.POST['cv']
        teacher= Teacher(name=name,number_phone=number_phone,email=email,cv=cv)
        teacher.save()
        messages.success(request, "Đăng ký thành công")
        return redirect('/')

