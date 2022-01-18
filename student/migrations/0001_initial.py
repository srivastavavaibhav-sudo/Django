# Generated by Django 4.0.1 on 2022-01-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('Date_of_birth', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]