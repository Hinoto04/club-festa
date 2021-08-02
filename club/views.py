
from django.shortcuts import render
from .models import Club

def index(request):
    """클럽 목록 출력"""
    club_list = Club.objects.order_by('name')
    context = {'club_list':club_list}
    return render(request, 'club/club_list.html', context)

def detail(request, club_id):
    """클럽 상세 출력"""
    club = Club.objects.get(id=club_id)
    context = {'club':club}
    return render(request, 'club/club_detail.html', context)