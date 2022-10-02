from django.shortcuts import render
from .forms import StudentForm,TeacherForm

# Create your views here.

def student_data(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentForm()
    return render(request,'enroll/student.html',{'form':fm})

def teacher_data(request):
    if request.method == "POST":
        fm = TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TeacherForm()
    return render(request,'enroll/teacher.html',{'form':fm})