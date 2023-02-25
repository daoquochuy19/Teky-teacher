# Generated by Django 4.0.6 on 2022-07-27 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BecomeLecturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='img/%y')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
