
from django.http.response import HttpResponse, JsonResponse
from config.pd_setting import CURRENT_YEAR
import config.settings as settings
from home.models import User
from django.shortcuts import redirect, render
from .models import Club
from django.core.paginator import Paginator
from django.contrib.auth.models import User as djangoUser

category = {'korean':'국어',
            'math':'수학',
            'english':'영어',
            'science':'과학',
            'society':'사회',
            'etc':'기타'}

def index(request):
    """클럽 목록 출력"""
    page = request.GET.get('page', '1')
    official = request.GET.get('official', '2')
    categoryeng = request.GET.get('category', 'all')
    club_list = Club.objects.all()
    club_list = Club.objects.filter(year=CURRENT_YEAR)
    if categoryeng != 'all':
        club_list = club_list.filter(category=category[categoryeng])
    if official == '0':
        club_list = club_list.filter(isofficial=False)
    elif official == '1':
        club_list = club_list.filter(isofficial=True)
    club_list = club_list.order_by('name')
    last = len(club_list)//9 if len(club_list) == 0 else len(club_list)//9+1
    
    paginator = Paginator(club_list, 9)
    page_obj = paginator.get_page(page)
    
    context = {'club_list':page_obj, 'last':last}
    return render(request, 'club/club_list.html', context)

def detail(request, club_id):
    """클럽 상세 출력"""
    try:
        club = Club.objects.get(id=club_id)
    except:
        return render(request, 'error.html', {'text': "동아리가 존재하지 않습니다."})
    else:
        member_list = []
        if club.member_detail != '':
            member_ids = club.member_detail.split(',')
            for member_id in member_ids:
                try:
                    member = User.objects.get(django_user = djangoUser.objects.get(id=member_id))
                except:
                    pass
                else:
                    member_list.append(member)
        context = {
            'club':club,
            'member_list': member_list,
            }
        return render(request, 'club/club_detail.html', context)

def update(request, club_id):
    try:
        club = Club.objects.get(id=club_id)
    except:
        return render(request, 'error.html', {'text':['동아리가 존재하지 않습니다.']})
    else:
        if request.user.is_authenticated:
            if club.club_master == User.objects.get(django_user=request.user):
                if request.method == 'GET':
                    memberlist = []
                    if club.member_detail != '':
                        for i in map(int,club.member_detail.split(',')):
                            try:
                                memberlist.append(User.objects.get(
                                    django_user = djangoUser.objects.get(id=i)
                                ))
                            except:
                                pass
                    applilist = []
                    if club.appli != '':
                        for i in map(int,club.appli.split(',')):
                            try:
                                applilist.append(User.objects.get(
                                    django_user = djangoUser.objects.get(id=i)
                                ))
                            except:
                                pass
                    context = {
                        'club': club,
                        'memberlist': memberlist,
                        'applilist': applilist
                    }
                    return render(request, 'club/club_update.html', context)
                else:
                    club.club_thumbnail = str(request.POST.get('thumbnail'))
                    club.category = category[str(request.POST.get('category'))]
                    club.description = str(request.POST.get('description'))
                    club.save()
                    return redirect('club:detail', club.id)
            else:
                return render(request, 'error.html', {'text':['권한이 없습니다.']})
        else:
            return render(request, 'error.html', {'text': ['로그인 되어 있지 않습니다.']})

def appli(request, club_id):
    if request.user.is_authenticated:
        user = request.user
        try:
            club = Club.objects.get(id=club_id)
        except:
            return render(request, 'error.html', {'text':['동아리가 존재하지 않습니다.']})
        else:
            if club.year != CURRENT_YEAR:
                return render(request, 'error.html', {'text':['올해 동아리에만 가입할 수 있습니다.']})
            if club.isofficial:
                for c in Club.objects.filter(isofficial=True).filter(year=CURRENT_YEAR):
                    if c.member_detail != '' and str(user.id) in c.member_detail.split(','):
                        return render(request, 'error.html', {'text':['이미 동아리에 가입되어 있습니다.']})
            if club.member_detail != '' and str(user.id) in club.member_detail.split(','):
                return render(request, 'error.html', {'text':['이미 해당 동아리에 가입되어 있습니다.']})
            if club.appli != '' and str(user.id) in club.appli.split(','):
                return render(request, 'error.html', {'text':['이미 해당 동아리에 신청했습니다.']}) 
            a = club.appli.split(',')
            a.append(str(user.id))
            club.appli = ','.join(a)
            club.save()
            return redirect('club:detail', club.id)
    else:
        return render(request, 'error.html', {'text': ['로그인 되어 있지 않습니다.']})

def accept(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            try:
                club = Club.objects.get(id=request.POST.get('clubid'))
            except:
                return JsonResponse({"result":"ClubNotFoundError"})
            if club.club_master == User.objects.get(django_user=user):
                userid = request.POST.get('userid')
                if club.appli != '' and str(userid) in club.appli.split(','):
                    d = club.appli.split(',')
                    d.remove(str(userid))
                    club.appli = ','.join(d)
                else:
                    return JsonResponse({"result":"NotAppliedError"})
                if request.POST.get('bool') == 'true':
                    if club.member_detail != '':
                        a = club.member_detail.split(',')
                    else:
                        a = []
                    a.append(str(userid))
                    club.member_detail = ','.join(a)
                    if club.isofficial:
                        for c in Club.objects.filter(isofficial=True).filter(year=CURRENT_YEAR):
                            if c.appli != '' and str(userid) in c.appli.split(','):
                                b = c.appli.split(',')
                                b.remove(str(userid))
                                c.appli = ','.join(b)
                                c.save()
                    club.save()
                return JsonResponse({"result":"success"})
            else:
                return JsonResponse({"result":"PermissionError"})
        else:
            return JsonResponse({"result":"NotLoggedInError"})
    else:
        return render(request, 'error.html', {'text':['이 페이지는 비활성화 되어 있습니다.']})
        