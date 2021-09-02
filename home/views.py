
from datetime import datetime
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, djangoUserForm, profileForm
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
                    return HttpResponse("""<pre>
유효하지 않은 값입니다.

1. 비밀번호 확인을 잘못 입력한 경우
2. 비밀번호가 너무 짧거나 안전하지 않은 경우
3. 이메일이 이미 사용된 경우
</pre>""")
            else:
                return HttpResponse("중복된 아이디입니다.")
        else:
            return HttpResponse("유효하지 않은 값입니다.")
    else:
        form = UserForm()
        return render(request, 'home/home_register.html', {'form':form})

def login(request):
    return render(request, 'home/home_login.html')

def user(request, userid = None):
    if userid:
        try:
            user = User.objects.get(django_user = djangoUser.objects.get(id=userid))
        except:
            return HttpResponse("존재하지 않는 유저입니다.")
        else:
            context = {
                'myuser': user
            }
            return render(request, 'home/home_user.html', context)
    else:
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
        'data':'not exist' if user is None and request.GET['username'] != '' else 'exist'
    }
    return JsonResponse(result)

def edit(request):
    if request.user.is_authenticated:
        user = User.objects.get(django_user = request.user)
        if request.method == 'POST':
            user.profile_message = str(request.POST.get('profilemessage'))
            user.interested_in = str(request.POST.get('interestedin'))
            user.description = request.POST.get('description')
            user.last_edit = datetime.now
            user.save()
            return redirect('home:index')
        else:
            context = {
                'myuser': user
            }
            return render(request, 'home/home_edit.html', context)
    else:
        return HttpResponse("로그인 되어있지 않습니다.")