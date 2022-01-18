from django.shortcuts import render
from .forms import CreateStudentForm
from .models import Student
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import authenticate, login

# Create your views here.

def CreateStudent(request):
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CreateStudentForm()
            return redirect('std_detail/')
    else:
        form = CreateStudentForm()

    students = Student.objects.all().order_by("-id")
    context = {'form':form, 'students':students}
    return render(request, 'home.html', context)


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

from django.contrib.auth import authenticate, login


def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect (f'/std_detail')
        # Redirect to a success page.
        ...
    else:
        return render(request, 'login.html')
        # Return an 'invalid login' error message.        