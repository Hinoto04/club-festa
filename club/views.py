
from django.shortcuts import render
from .models import Club
from django.core.paginator import Paginator

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
    context = {'club':club}
    return render(request, 'club/club_detail.html', context)