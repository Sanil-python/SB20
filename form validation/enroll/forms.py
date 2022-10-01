from django import forms
from django.core import validators

# def starts_with_s(name):
#     if name[0]!='s':
#         raise forms.ValidationError('Name should start with s')
    
class StudentForm(forms.Form):
    # name = forms.CharField(validators=[starts_with_s])
    # name = forms.CharField(validators=[validators.MinLengthValidator(5)])
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)',widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password']
        valrpwd =self.cleaned_data['rpassword']
        if valpwd != valrpwd:
            raise forms.ValidationError("Password is not matching")