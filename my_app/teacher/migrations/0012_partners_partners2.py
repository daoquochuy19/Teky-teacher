# Generated by Django 4.0.6 on 2022-07-29 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_registerteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Partners2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
