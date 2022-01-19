from django.db import models

# Create your models here.
class Stream(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.class_name}'

class Student(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=10)
    age = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=20)
    Date_of_birth = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default=False)
    password = models.CharField(max_length=20, blank=True)
    
    image = models.CharField(max_length=100) #Charfield is used for storing url of AWS image data that's why i used Charfield.
    student_class = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name}'