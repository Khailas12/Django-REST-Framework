# Generated by Django 3.2.7 on 2021-10-10 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thep', '0002_student_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='place',
        ),
    ]
