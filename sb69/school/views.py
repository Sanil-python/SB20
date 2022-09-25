from django.shortcuts import render
from .models import ExamCenter,ProxyExamCenter

# Create your views here.

def home(request):
    ecs = ExamCenter.objects.all()
    pecs = ProxyExamCenter.objects.all()
    return render(request, 'school/home.html', {'ecs':ecs,'pecs':pecs})