from distutils.command.upload import upload
import email
from email.mime import image
from statistics import mode
from turtle import title
from django.forms import CharField
from django.db import models
from django.contrib.auth.models import User


class BecomeLecturers(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")
    content=models.CharField(max_length=200)
class TutorBlock(models.Model):
    image=models.ImageField(upload_to="img/%y", blank=True, null=True) 
    title=models.CharField(max_length=200, blank=True, null=True) 
    content=models.CharField(max_length=200, blank=True, null=True)
class TutorBlock2(models.Model):
    title=models.CharField(max_length=200) 
    content=models.CharField(max_length=200) 
class TutorIcon(models.Model):
    image=models.ImageField(upload_to="img/%y") 
    title=models.CharField(max_length=200) 
    content=models.CharField(max_length=200)
class TutorIcon2(models.Model):
    image=models.ImageField(upload_to="img/%y") 
class WhyMakeTeacher(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")
    content=models.CharField(max_length=200)
class WhyMakeTeacher2(models.Model):
    image=models.ImageField(upload_to="img/%y")
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
class ActivitiesCultural(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")
    content=models.CharField(max_length=200)
class ActivitiesCultural2(models.Model):
    image=models.ImageField(upload_to="img/%y")
class AboutUs(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")
    content=models.CharField(max_length=200)
class AboutUs2(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")
    name=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
class RegisterTeacher(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="img/%y")
    content=models.CharField(max_length=200)
class Partners(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
class Partners2(models.Model):
    image=models.ImageField(upload_to="img/%y")

class Teacher(models.Model):
    name=models.CharField(max_length=200)
    number_phone= models.IntegerField()
    email=models.CharField(max_length=200)
    cv=models.FileField(upload_to ='cv/%y')