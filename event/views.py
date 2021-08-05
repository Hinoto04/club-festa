
from django.shortcuts import render

def index(request):
    return render(request, 'event/event_test.html')

##    return render("이밴트 목록은 준비중입니다.....")
