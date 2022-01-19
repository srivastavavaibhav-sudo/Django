from curses.ascii import CR
from django.urls import path
from .views import Retrieve_ListView, UpdateView, login, Create,Add_class

urlpatterns = [
    path('login', login),
    path('create', Create),
    path('', Add_class),
    path('std_detail', Retrieve_ListView, name='student_details'),
    path('data/<int:_id>/update', UpdateView),

]