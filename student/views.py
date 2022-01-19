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
    stu = {
    "class": data
        }
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
        # all_class = Stream.objects.all()
        student_data = Student(first_name=first_name,
                                last_name=last_name,
                                phone=phone, 
                                age=age,
                                email=email,
                                Date_of_birth=Date_of_birth,
                                status=status,
                                password=password,
                                image=image,
                                )
        student_data.save()
        return redirect('std_detail/')    
    return render(request, 'stud_create.html', stu)




def Retrieve_ListView(request):
    dataset = Student.objects.all()
    return render(request,'index.html',{'dataset':dataset})


def UpdateView(request,_id):
    try:
        old_data = get_object_or_404(Student,id =_id)
    except Exception:
        raise Http404('Does Not Exist')
 
    if request.method =='POST':
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





def login(request, id):
    check_user = Student.objects.get(id=id)
    first_name = request.POST.get('first_name', False)
    password = request.POST.get('password', False)
    user = Student(first_name==first_name , password==password)
    if user:
        print("vaibhav")
    else:
        print("mohit")

    return render (request, 'login.html')                

   
