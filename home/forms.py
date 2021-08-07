from django import forms

class UserForm(forms.Form):
    email = forms.EmailField(label='이메일')
    username = forms.CharField(max_length=32, label='아이디')
    name = forms.CharField(max_length=20, label='이름')
    number = forms.IntegerField(label='학번')
    password1 = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
    password2 = forms.CharField(widget=forms.PasswordInput, label='비밀번호 확인')
    
    fields = ['email', 'username', 'name', 'number', 'password1', 'password2']
    
    def clean(self):
        cleaned_data = super().clean()