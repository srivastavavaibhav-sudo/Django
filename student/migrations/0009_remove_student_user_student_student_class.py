# Generated by Django 4.0.1 on 2022-01-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
