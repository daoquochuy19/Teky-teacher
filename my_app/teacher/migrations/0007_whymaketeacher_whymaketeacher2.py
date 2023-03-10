# Generated by Django 4.0.6 on 2022-07-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_tutorblock2_tutoricon_tutoricon2'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyMakeTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/%y')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WhyMakeTeacher2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
