from django.urls import path
from .views import CreateStudent, Retrieve_ListView, UpdateView, login

urlpatterns = [
    path('', CreateStudent, name='create_student'),
    path('std_detail/', Retrieve_ListView, name='student_details'),
    path('data/<int:_id>/update', UpdateView),
    path('login', login),

]