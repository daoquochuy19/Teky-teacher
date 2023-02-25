from django.contrib import admin
from .models import AboutUs, AboutUs2, ActivitiesCultural, ActivitiesCultural2, BecomeLecturers, Partners, Partners2, RegisterTeacher, Teacher, TutorBlock, TutorBlock2, TutorIcon, TutorIcon2, WhyMakeTeacher, WhyMakeTeacher2
from tkinter.tix import IMAGE


class TutorBlockAdmin(admin.ModelAdmin):
    list_display = ['image','title','content']
    list_per_page = 10


class TutorIcon2Admin(admin.ModelAdmin):
    list_display = ['image']
    list_per_page = 10


class AboutUS2Admin(admin.ModelAdmin):
    list_display = ['title','image','name','position']
    list_per_page = 10
class Partners2Admin(admin.ModelAdmin):
    list_display = ['image']
    list_per_page = 10

admin.site.register(BecomeLecturers)
admin.site.register(TutorBlock, TutorBlockAdmin)
admin.site.register(TutorBlock2)
admin.site.register(TutorIcon)
admin.site.register(TutorIcon2,TutorIcon2Admin)
admin.site.register(WhyMakeTeacher)
admin.site.register(WhyMakeTeacher2)
admin.site.register(ActivitiesCultural)
admin.site.register(ActivitiesCultural2)
admin.site.register(AboutUs)
admin.site.register(AboutUs2)
admin.site.register(RegisterTeacher)
admin.site.register(Partners)
admin.site.register(Partners2,Partners2Admin)
admin.site.register(Teacher)


