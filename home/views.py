
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as djangoUser
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'home/home_main.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        userForm = UserCreationForm(request.POST)
        if form.is_valid() and userForm.is_valid:
            form.clean()
            userForm.save()
            user = User(name=form.cleaned_data.get('name'), 
                        number=form.cleaned_data.get('number'),
                        regi_date = timezone.now(),
                        type = 'Student',
                        email = form.cleaned_data.get('email'))
            user.save()
            
            
            #userForm.username = form.username
            #userForm.password1 = form.password1
            #userForm.password2 = form.password2
            loginuser = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(loginuser)
            return redirect('home:index')
            """
            djangouser = djangoUser(username = form.cleaned_data.get('id'),
                                    password = form.password1,
                                    email = form.cleaned_data.get('email'))
            djangouser.save()
            """
    else:
        form = UserForm()
        return render(request, 'home/home_register.html', {'form':form})

def login(request):
    return render(request, 'home/home_login.html')

def myPage(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        context = {
            'myuser': user
        }
        return render(request, 'home/home_myPage.html', context)
    else:
        return HttpResponse("로그인 되어있지 않습니다.")
    