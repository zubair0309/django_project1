from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Marks,Student
from django.contrib.auth.models import User
#from .forms import degisterForm,Register
# Create your views here.
def basic_demo(request):
    students= Student.objects.all()
    return render(request,'basic.html',{'students':students})
def add(request):
     message=""
     if request.method=="POST":
       Student.objects.create(
        name=request.POST['name'],
        age=request.POST['age'],
        roll_no=request.POST['roll_no'],
        contact=request.POST['contact'],
        )
       name=request.POST['name']
       Marks.objects.create(
        student=Student.objects.get(name=name),
        Telugu=request.POST['telugu'],
        Hindi=request.POST['hindi'],
        English=request.POST['english'],
        Science=request.POST['science'],
        )
       message="Student Added Successfully"
     return render(request,'add.html',{'message':message})
def update(request):
     message=""
     search_term=request.GET.get('search_term')
     student = Student.objects.get(roll_no=search_term)
     marks = Marks.objects.get(student=student)
     if request.method=="POST":
        student.name=request.POST['name']
        student.age=request.POST['age']
        student.contact=request.POST['contact']
        student.save()
        marks.Telugu=request.POST['telugu']
        marks.Hindi=request.POST['hindi']
        marks.English=request.POST['english']
        marks.Science=request.POST['science']
        marks.save()
        message="Student Updated Successfully" 
     return render(request,'update.html',{'message':message,'marks':marks,'student':student})
def form(request):
     return render(request,'form.html')
def view(request):
     students=Student.objects.all()
     return render(request,'views.html',{'students':students})
def delete(request, roll_no):
   std=get_object_or_404(Student,roll_no=roll_no)
   std.delete()
   return redirect("view_students")
    
def search(request):
     if request.method=="POST":
       roll_no=request.POST.get('roll')
       student=Student.objects.get(roll_no=roll_no)
       marks=Marks.objects.get(student=student)
       if student:
         return render(request,'data.html',{'student':student,'marks':marks})
     return render(request,'search.html')