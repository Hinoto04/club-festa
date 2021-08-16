
from home.models import User
from django.shortcuts import render
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
    club = Club.objects.get(id=club_id)
    member_ids = club.member_detail.split(',')
    member_list = []
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