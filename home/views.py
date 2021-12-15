
from datetime import datetime
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text

from config.pd_setting import CURRENT_YEAR
from .tokens import account_activation_token
from .forms import UserForm, djangoUserForm, profileForm
from .models import User, UserLoginLog
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as djangoUser
from django.contrib.auth.forms import UserCreationForm
from club.models import Club
from ipware.ip import get_client_ip
from post.models import Notice, Post
from django.db.models import Q
import numpy as np
from event.models import Event
from datetime import timedelta, date, time, timezone as tz

def findclub(user):
    clubs = []
    for club in Club.objects.filter(year=CURRENT_YEAR):
        if user.id in map(int, club.member_detail.split(',')):
            clubs.append(club)
    return clubs

def index(request):
    class day():
        
        def __init__(self, date):
            self.date = date
            self.event = False
            self.today = False
        
        def __str__(self):
            return self.event
        
        def __repr__(self):
            return str(self.event)
        
    if request.user.is_authenticated:
        log = UserLoginLog(
            user = User.objects.get(django_user=request.user),
            ip_address = get_client_ip(request),
            logged = timezone.now()
        )
        log.save()
    q = Q()
    q.add(Q(hotDate__gte=timezone.localtime()), q.AND)
    q.add(Q(publicDate__lte=timezone.localtime()), q.AND)
    notice_list = Notice.objects.order_by('-create_date').filter(q)[:3]
    hot_list = Post.objects.order_by('-create_date').filter(isprivate=False, like__gte=5)[:3]
    
    #행사 목록 불러오는 코드
    today = timezone.localtime()
    startdate = date(year = today.year, month = today.month, day=1)
    
    mt = (startdate.weekday()+1)%7 # 월요일==0+1 .... 일요일==6+1
    startdate = startdate - timedelta(days = mt)  #달력의 공칸 만큼 시작일 연기()
    
    sd = datetime.combine(startdate, time(), tz(timedelta(hours=9)))
    events = Event.objects.filter(start_date__gte=sd).filter(end_date__lte=sd+timedelta(days=35)).order_by('start_date')
    
    month = []
    for i in range(35):
        month.append(day(startdate + timedelta(days = i)))
    for event in events:
        for d in month:
            if event.start_date <= d.date <= event.end_date:
                d.event = True
            if d.date == event.end_date:
                break
    for d in month:
        if today.date() == d.date:
            d.today = True
    month = np.reshape(month, (5,7))
    
    #html로 보낼 거
    context = {
        'notice_list': notice_list,
        'hot_list': hot_list,
        'month': month,
    }
    return render(request, 'home/home_main.html', context)

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.clean()
            try:
                djangoUser.objects.get(username=form.cleaned_data.get('username'))
            except:
                userForm = djangoUserForm(request.POST
#                   username = request.POST.get('username'),
#                   password1 = request.POST.get('password1'),
#                   password2 = request.POST.get('password2'),
#                   email = request.POST.get('email')
                )
                if userForm.is_valid():
                    nowuser = userForm.save()
                    nowuser.save()
                    nowuser.is_active = False
                    nowuser.save()
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
                    log = UserLoginLog(
                        user = user,
                        ip_address = get_client_ip(request),
                        logged = timezone.now()
                    )
                    log.save()
                    message = render_to_string('home/activation_email.html',
                        {
                            'user': nowuser,
                            'domain': request.get_host(),
                            'uid': urlsafe_base64_encode(force_bytes(nowuser.pk)),
                            'token': account_activation_token.make_token(nowuser),
                        })
                    mail_title = "계정 활성화 확인 이메일"
                    email = EmailMessage(mail_title, message, to=[nowuser.email])
                    email.send()
                    
                    #userForm.username = form.username
                    #userForm.password1 = form.password1
                    #userForm.password2 = form.password2
                    #loginuser = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
                    #login(loginuser)
                    return redirect('home:login')
                    """
                    djangouser = djangoUser(username = form.cleaned_data.get('id'),
                                            password = form.password1,
                                            email = form.cleaned_data.get('email'))
                    djangouser.save()
                    """
                else:
                    return render(request, 'error.html', {'text': 
["유효하지 않은 값입니다.",
"1. 비밀번호 확인을 잘못 입력한 경우",
"2. 비밀번호가 너무 짧은 경우",
"3. 이메일이 이미 사용된 경우",
]})
            else:
                return render(request, 'error.html', {'text': ["중복된 아이디입니다."]})
        else:
            return render(request, 'error.html', {'text': ["유효하지 않은 값입니다."]})
    else:
        form = UserForm()
        return render(request, 'home/home_register.html', {'form':form})

def login(request):
    return render(request, 'home/home_login.html')

def user(request, userid = None):
    if userid:
        try:
            du = djangoUser.objects.get(id=userid)
            user = User.objects.get(django_user = du)
            clubs = findclub(du)
        except:
            return render(request, 'error.html', {'text': ["존재하지 않는 유저입니다."]})
        else:
            context = {
                'myuser': user,
                'clubs': clubs
            }
            return render(request, 'home/home_user.html', context)
    else:
        if request.user.is_authenticated:
            user = User.objects.get(django_user = request.user)
            clubs = findclub(request.user)
            context = {
                'myuser': user,
                'clubs': clubs
            }
            return render(request, 'home/home_user.html', context)
        else:
            return render(request, 'error.html', {'text':[ "로그인 되어 있지 않습니다."]})

def checkmail(request):
    try:
        user = djangoUser.objects.get(username=request.GET['username'])
    except Exception as e:
        user = None
    result = {
        'result':'success',
        'data':'not exist' if user is None and len(request.GET['username']) >= 5 else 'exist'
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
        return render(request, 'error.html', {'text': ["로그인 되어 있지 않습니다."]})

def manage(request):
    if request.user.is_authenticated:
        user = User.objects.get(django_user = request.user)
        club_list = Club.objects.filter(club_master=user)
        context = {
            'club_list': club_list
        }
        return render(request, 'home/home_manage.html', context)
    else:
        return render(request, 'error.html', {'text':['로그인 되어 있지 않습니다.']})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = djangoUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request)
        return redirect('home:index')
    else:
        return render(request, 'error.html', {'text':['계정 활성화 오류']})

def accountcreate(request):
    return render(request, 'error.html', {'text':['활성화되지 않은 기능입니다.']})