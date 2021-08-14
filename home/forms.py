from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as djangoUser

class UserForm(forms.Form):
    email = forms.EmailField(label='이메일')
    username = forms.CharField(max_length=32, label='아이디')
    name = forms.CharField(max_length=20, label='이름')
    number = forms.IntegerField(label='학번')
    password1 = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
    password2 = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')
    
    fields = ('email', 'username', 'name', 'number', 'password1', 'password2')
    
    def clean(self):
        cleaned_data = super().clean()
        
class djangoUserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    
    class Meta:
        model = djangoUser
        fields = ("username", "password1", "password2", "email")
        
class profileForm(forms.Form):
    profile_message = forms.CharField(max_length=200)
    interested_in = forms.CharField(max_length=20)
    description = forms.CharField()
    
    fields = ('profile_message', 'interested_in', 'description')
    
    def clean(self):
        cleaned_data = super().clean()