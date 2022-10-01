from django.shortcuts import render
from .forms import StudentForm

# Create your views here.

def studentformdata(request):
    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print('Form validated')
            print('Name: ', fm.cleaned_data['name'])
            print('Email: ', fm.cleaned_data['email'])
            print('Password: ', fm.cleaned_data['password'])
            print('RPassword: ', fm.cleaned_data['rpassword'])
            
    else:
        fm = StudentForm()
        
    return render(request,'enroll/studentregistration.html',{'form':fm})