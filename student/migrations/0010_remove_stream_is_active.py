# Generated by Django 4.0.1 on 2022-01-19 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_remove_student_user_student_student_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='is_active',
        ),
    ]
