from django.shortcuts import render
from .forms import CreateStudentForm
from .models import Student, Stream
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

# adding new class in database
def Add_class(request):
    if request.method == "POST":        
        class_name = request.POST['class_name']
        add_class = Stream(class_name=class_name)
        add_class.save()
        return redirect('/create')    
    return render(request, 'create_class.html',)


# adding new Student in database
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
        return redirect('/student_login/')    
    return render(request, 'stud_create.html', stu)


# Student detail 
def Retrieve_ListView(request):
    # query to get all student data from database
    dataset = Student.objects.all()
    return render(request,'index.html',{'dataset':dataset})

# updating data of Student
def UpdateView(request,_id):
    # query to filter student data from database
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

   
def user_login(request):
    if request.method == "POST":            
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        print(first_name , password)
        # query to filter inactive stage of student from database
        obj = Student.objects.filter(first_name = first_name)\
                                .filter(password = password)\
                                .filter(is_active = True).all()
        if obj:
            messages.success(request, 'You login successfully!')
            return redirect('/std_detail')
        else:  
            # pass      
            messages.success(request, 'Invalid Cridential! OR activate student from admin ')
            return render(request, 'login1.html')
    return render(request, 'login1.html' )
 