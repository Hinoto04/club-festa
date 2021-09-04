from django.http.response import HttpResponse
from post.models import Notice, Post
from home.models import User
from club.models import Club
from django.db.models import Q
import datetime
from django.shortcuts import render
from django.core.paginator import Paginator

def index(request):
    page = request.GET.get('page', '1')
    filter = request.GET.get('view', None)
    if filter is None or filter == 'all':
        notice_list = Notice.objects.order_by('-create_date').filter(isHot=True)[:5]
        post_list = Post.objects.order_by('-create_date').filter(isprivate=False)
    elif filter == 'notice':
        notice_list = Notice.objects.order_by('-create_date')
        post_list = None
    elif filter == 'club':
        if request.user:
            clubs = []
            for club in Club.objects.all():
                if request.user.id in map(int, club.member_detail.split(',')):
                    clubs.append(club)
            q = Q()
            for club in clubs:
                q.add(Q(club=club), q.OR)
            notice_list = None
            post_list = Post.objects.order_by('-create_date').filter(q, isprivate=False)
        else:
            notice_list = Notice.objects.order_by('-create_date').filter(isHot=True)[:5]
            post_list = Post.objects.order_by('-create_date').filter(isprivate=False)
    elif filter == 'hot':
        notice_list = None
        post_list = Post.objects.order_by('-create_date').filter(isprivate=False, like__gte=5)
    if post_list:
        paginator = Paginator(post_list, 20)
        post_list = paginator.get_page(page)
    context = {
        "notice_list" : notice_list,
        "post_list" : post_list,
    }
    return render(request, 'post/post_list.html', context)

def postdetail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return HttpResponse("게시글이 존재하지 않습니다.")
    return render(request, 'post/post_detail.html', {"post": post})

def noticedetail(request, notice_id):
    try:
        post = Notice.objects.get(id=notice_id)
    except:
        return HttpResponse("게시글이 존재하지 않습니다.")
    return render(request, 'post/post_detail.html', {"post":post})

def testcase(request):
    for i in range(50):
        post = Post(title='테스트:[%03d]'%i, 
                    description='테스트내용', 
                    isprivate=False, 
                    isnotice=False, 
                    club=Club.objects.get(id=1), 
                    author=User.objects.get(id=1), 
                    views=0, 
                    like=0, 
                    create_date=datetime.datetime.now())
        post.save()
    return HttpResponse("테스트케이스 생성 완료")