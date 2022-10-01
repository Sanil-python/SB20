from django.shortcuts import render
from .forms import StudentForm
from .models import Student

# Create your views here.

def studentregistration(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            
            #To save and update datas into the database 
            # reg = Student(id=2, name=nm, email=em, password=ps)
            # reg.save()
            
            # To delete datas in the database
            reg = Student(id=2)
            reg.delete()
            
    else:
        fm = StudentForm()
    return render(request, 'enroll/studentregistration.html', {'form':fm})