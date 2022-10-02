from django import forms
from .models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id','student_name','email','password']
        
class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = ['id','teacher_name','email','password']