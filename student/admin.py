from django.contrib import admin

# Register your models here.
from student.models import Student, Stream
# Register your models here.
admin.site.register(Student)
admin.site.register(Stream)