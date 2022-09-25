from django.shortcuts import render
from .models import ExamCenter,Student

# Create your views here.

def home(request):
    ecenters = ExamCenter.objects.all()
    students = Student.objects.all()
    return render(request, 'school/home.html', {'ecenters':ecenters, 'students':students})