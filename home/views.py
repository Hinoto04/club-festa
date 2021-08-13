
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, djangoUserForm
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
        if form.is_valid():
            form.clean()
            try:
                checkuser = djangoUser.objects.get(username=form.cleaned_data.get('username'))
            except:
                userForm = djangoUserForm(request.POST
#                   username = request.POST.get('username'),
#                   password1 = request.POST.get('password1'),
#                   password2 = request.POST.get('password2'),
#                   email = request.POST.get('email')
                )
                if userForm.is_valid():
                    nowuser = userForm.save()
                    #nowuser = djangoUser.objects.order_by('id')
                    user = User(name=form.cleaned_data.get('name'), 
                                number=form.cleaned_data.get('number'),
                                regi_date = timezone.now(),
                                type = 'Student',
                                email = form.cleaned_data.get('email'),
                                django_user = nowuser,
                                profile_message = '',
                                interested_in = '',
                                description = '')
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
                    return HttpResponse("비밀번호가 잘못되었거나, 유효하지 않은 값입니다.")
            else:
                return HttpResponse("중복된 아이디입니다.")
        else:
            return HttpResponse("유효하지 않은 값입니다.")
    else:
        form = UserForm()
        return render(request, 'home/home_register.html', {'form':form})

def login(request):
    return render(request, 'home/home_login.html')

def user(request):
    if request.user.is_authenticated:
        user = User.objects.get(django_user = request.user)
        context = {
            'myuser': user
        }
        return render(request, 'home/home_user.html', context)
    else:
        return HttpResponse("로그인 되어있지 않습니다.")

def checkmail(request):
    try:
        user = djangoUser.objects.get(username=request.GET['username'])
    except Exception as e:
        print(e)
        user = None
    result = {
        'result':'success',
        'data':'not exist' if user is None else 'exist'
    }
    return JsonResponse(result)