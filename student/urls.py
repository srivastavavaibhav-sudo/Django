from django.urls import path
from .views import Retrieve_ListView, UpdateView, Create,Add_class, user_login

urlpatterns = [        

    path('student_login/', user_login), #url for student login
    path('create', Create), # url for add new student
    path('', Add_class), # url for add new class 
    path('std_detail/', Retrieve_ListView, name='student_details'), # url for details of student
    path('data/<int:_id>/update', UpdateView), # url for edit student detail

]