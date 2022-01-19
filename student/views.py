from http.client import HTTPResponse
from pickle import FALSE
import re
from django.shortcuts import render
from .forms import CreateStudentForm
from .models import Student, Stream
from django.shortcuts import redirect,get_object_or_404,Http404

# Create your views here.


def Add_class(request):
    if request.method == "POST":
        
        class_name = request.POST['class_name']
        add_class = Stream(class_name=class_name)
        add_class.save()
        return redirect('/create')    
    return render(request, 'create_class.html',)

def Create(request):
    data = Stream.objects.all()
    stu = {"class": data}

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        age = request.POST['age']
        email = request.POST['email']
        Date_of_birth = request.POST['Date_of_birth']
        status = request.POST['status']
        password = request.POST['password']
        image = request.POST['image']
        all_class = request.POST['all_class']
        student_data = Student(first_name=first_name,
                                last_name=last_name,
                                phone=phone, 
                                age=age,
                                email=email,
                                Date_of_birth=Date_of_birth,
                                status=status,
                                password=password,
                                image=image,
                                student_class=all_class
                                )
        student_data.save()
        return redirect('login/')    
    return render(request, 'stud_create.html', stu)




def Retrieve_ListView(request):
    dataset = Student.objects.all()
    return render(request,'index.html',{'dataset':dataset})


def UpdateView(request,_id):
    old_data = Student.objects.get(id = _id)
    form =CreateStudentForm(request.POST, instance =old_data)
    
    if form.is_valid():
        form.save()
        return redirect(f'/std_detail')
        
    else:
    
        form = CreateStudentForm(instance = old_data)
        context ={
                'form':form
                }
        return render(request,'update.html',context)    



def login(request):
    
    first_name = request.POST.get('first_name')
    password = request.POST.get('password')
    print(first_name,password)
    return render(request, 'login.html')
    # first_name = request.POST['first_name']
    # password = request.POST['password']
    # print(first_name,password)
    # from django.contrib import auth
    # # user = auth.authenticate(first_name=first_name , password=password)
    # user = Student(first_name=first_name , password=password)
    # print(user)
    # if user is not None:
    #     return redirect('std_detail/')
    # else:
    #     # return redirect ('/')       
    #     return render (request, 'login.html')                

   

 