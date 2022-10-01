from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','email','password']
        widgets = {'password':forms.PasswordInput}