from django.http.response import HttpResponse, JsonResponse
from post.models import Comment, Notice, Post
from home.models import User
from club.models import Club
from django.contrib.auth.models import User as djangoUser
from django.db.models import Q
import datetime
from django.shortcuts import redirect, render, reverse
from django.core.paginator import Paginator

def findclub(user):
    clubs = []
    for club in Club.objects.all():
        if user.id in map(int, club.member_detail.split(',')):
            clubs.append(club)
    return clubs

def getLikeList(targetuser, type = "post"):
    user = User.objects.get(django_user=targetuser)
    if type == "post":
        ul = user.like.split('/')
    else:
        ul = user.noticelike.split('/')
    likelist = list(map(int, ul[0].split(','))) if len(ul[0])>0 else []
    unlikelist = list(map(int, ul[1].split(','))) if len(ul[1])>0 else []
    return likelist, unlikelist

def index(request):
    page = request.GET.get('page', '1')
    filter = request.GET.get('view', 'all')
    last = 1
    if filter == 'notice':
        notice_list = Notice.objects.order_by('-create_date')
        paginator = Paginator(notice_list, 20)
        notice_list = paginator.get_page(page)
        post_list = None
    elif filter == 'club':
        if request.user.is_authenticated:
            clubs = findclub(request.user)
            q = Q()
            for club in clubs:
                q.add(Q(club=club), q.OR)
            notice_list = None
            post_list = Post.objects.order_by('-create_date').filter(q)
        else:
            q = Q()
            q.add(Q(hotDate__gte=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))), q.AND)
            q.add(Q(publicDate__lte=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))), q.AND)
            notice_list = Notice.objects.order_by('-create_date').filter(q)[:5]
            post_list = Post.objects.order_by('-create_date').filter(isprivate=False)
    elif filter == 'hot':
        notice_list = None
        post_list = Post.objects.order_by('-create_date').filter(isprivate=False, like__gte=5)
    else:
        q = Q()
        q.add(Q(hotDate__gte=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))), q.AND)
        q.add(Q(publicDate__lte=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))), q.AND)
        notice_list = Notice.objects.order_by('-create_date').filter(q)[:5]
        post_list = Post.objects.order_by('-create_date').filter(isprivate=False)
    if post_list:
        paginator = Paginator(post_list, 20)
        post_list = paginator.get_page(page)
    context = {
        "notice_list" : notice_list,
        "post_list" : post_list,
        "last" : last,
        "mode" : filter
    }
    return render(request, 'post/post_list.html', context)

def postdetail(request, post_id):
    try:
        like = 0 
        if request.user.is_authenticated:
            likelist, unlikelist = getLikeList(request.user)
            if post_id in likelist:
                like = 1
            elif post_id in unlikelist:
                like = -1
        post = Post.objects.get(id=post_id)
        post.views += 1
        post.save()
        comment_list = Comment.objects.filter(post=post)
    except:
        return render(request, 'error.html', {'text': ["게시글이 존재하지 않습니다."]})
    context = {
        "post": post,
        "like": like,
        "comment_list": comment_list,
    }
    return render(request, 'post/post_detail.html', context)

def noticedetail(request, notice_id):
    try:
        like = 0 
        if request.user.is_authenticated:
            likelist, unlikelist = getLikeList(request.user, "notice")
            if notice_id in likelist:
                like = 1
            elif notice_id in unlikelist:
                like = -1
        post = Notice.objects.get(id=notice_id)
        post.views += 1
        post.save()
        comment_list = Comment.objects.filter(post=post)
    except:
        return render(request, 'error.html', {'text': ["게시글이 존재하지 않습니다."]})
    context = {
        "post": post,
        "like": like,
        "comment_list": comment_list,
    }
    return render(request, 'post/post_detail.html', context)

def write(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post(
                title = str(request.POST.get('title')),
                description = str(request.POST.get('description')),
                isprivate = bool(request.POST.get('isprivate')),
                author = User.objects.get(django_user=djangoUser.objects.get(id=request.user.id)),
                club = Club.objects.get(id=request.POST.get('club')),
                create_date = datetime.datetime.now()
            )
            post.save()
            return redirect(reverse('post:postdetail',args=[post.id]))
        else:
            clubs = findclub(request.user)
            context = {
                'clubs': clubs,
            }
            return render(request, 'post/post_write.html', context)
    else:
        return render(request, 'error.html', {'text': ["로그인 되어 있지 않습니다."]})

def like(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                if request.POST.get('posttype') == 'post':
                    post = Post.objects.get(id=request.POST.get('postid'))
                else:
                    post = Notice.objects.get(id=request.POST.get('postid'))
            except:
                return JsonResponse({"result":"failed"})
            else:
                if request.POST.get('posttype') == 'post':
                    likelist, unlikelist = getLikeList(request.user)
                else:
                    likelist, unlikelist = getLikeList(request.user, "notice")
                user = User.objects.get(django_user=request.user)
                if not (post.id in likelist or post.id in unlikelist):
                    if request.POST.get('like') == 'true':
                        post.like += 1
                        likelist.append(post.id)
                    else:
                        post.like -= 1
                        unlikelist.append(post.id)
                    if request.POST.get('posttype') == 'post':
                        user.like = ','.join(map(str, likelist))+'/'+','.join(map(str, unlikelist))
                    else:
                        user.noticelike = ','.join(map(str, likelist))+'/'+','.join(map(str, unlikelist))
                    user.save()
                    post.save()
                    return JsonResponse({"result":"success", "like":post.like, "change":"append"})
                else:
                    if request.POST.get('like') == 'false':
                        if post.id in likelist:
                            likelist.remove(post.id)
                            unlikelist.append(post.id)
                            change = "append"
                            post.like -= 2
                        else:
                            unlikelist.remove(post.id)
                            change = "remove"
                            post.like += 1
                    else:
                        if post.id in unlikelist:
                            likelist.append(post.id)
                            unlikelist.remove(post.id)
                            change = "append"
                            post.like += 2 
                        else:
                            likelist.remove(post.id)
                            change = "remove"
                            post.like -= 1
                    if request.POST.get('posttype') == 'post':
                        user.like = ','.join(map(str, likelist))+'/'+','.join(map(str, unlikelist))
                    else:
                        user.noticelike = ','.join(map(str, likelist))+'/'+','.join(map(str, unlikelist))
                    user.save()
                    post.save()
                    return JsonResponse({"result":"success", "like":post.like, "change":change})
            
        else:
            return JsonResponse({"result":"failed"})
    else:
        return render(request, 'error.html', {'text': ['해당 링크는 비활성화되어있습니다.']})
    
def commentwrite(request, post_id):
    if request.user.is_authenticated:
        try:
            if request.GET.get('type', 'post') == 'post':
                post = Post.objects.get(id=post_id)
            else:
                post = Notice.objects.get(id=post_id)
        except:
            return render(request, 'error.html', {'text':['글이 존재하지 않습니다.']})
        else:
            try:
                author = User.objects.get(django_user=request.user)
            except:
                return render(request, 'error.html', {'text':['사용자가 존재하지 않습니다.']})
            else:
                cmt = Comment(
                    content = str(request.POST.get('description')),
                    author = author,
                    create_date = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
                )
                if request.GET.get('type', 'post') == 'post':
                    cmt.post = post
                else:
                    cmt.notice = post
                cmt.save()
                return redirect(reverse('post:postdetail',args=[post.id]))
    else:
        return render(request, 'error.html', {'text':['로그인 되어 있지 않습니다.']})

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
    return render(request, 'error.html', {'text': ["테스트케이스 생성 완료"]})