# Generated by Django 3.0.6 on 2020-05-21 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200521_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogaplication',
            name='published_date',
        ),
    ]
