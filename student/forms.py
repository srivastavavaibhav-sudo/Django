from django import forms
from .models import Student 


class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['first_name','last_name','email','phone','age','Date_of_birth','status','password','image']