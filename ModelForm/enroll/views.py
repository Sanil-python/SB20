from django.shortcuts import render
from .forms import StudentModelForm
from .models import Student

# Create your views here.

def studentregistrationform(request,pk):
    if request.method == "POST":
        fm = StudentModelForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']

            reg = Student(name=nm,email=em,password=ps)
            reg = Student(id=1,name=nm,email=em,password=ps)
            reg.save()

        # reg = Student(id=1)
        # reg.delete()   
    else:
        fm = StudentModelForm()
    return render(request,'enroll/studentregistration.html',{'form':fm})