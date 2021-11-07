
from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from .models import Event
from .forms import EventForm

from datetime import date

def index(request, event_month=None):
    class day:
        date = None
        event = []
        
        def __init__(self, date):
            date = date
    
    #대충 첫 날짜
    #startdate = date.
    month = []
    #month에 주별로 day 추가
    #for i in range(5):
    #    week = []
    #    for j in range(7):
    #        week.append(day(date.))
    events = Event.objects.filter(start_date__year=2021).filter(start_date__month=11)|Event.objects.filter(end_date__year=2021).filter(end_date__month=11)
    #for event in events:
    #    날짜 확인 후 해당 날짜에 event 추가
    #    기간제인 경우 해당 기간의 모든 날짜에 event 추가
    
    context = {
        'year_month': '2021-11',
        'month': month
    }
    return render(request, 'event/event_main.html', context)

def registration(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('event:index') # 행사 등록 후 쓰고 달력으로 돌아감
        else:
            print(event_form)
    return render(request,'event/event_reg.html',{'event_form':EventForm()})

def detail(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except:
        return render(request, 'error.html', {'text':['이벤트가 존재하지 않습니다.']})
    else:
        return render(request, 'event/event_detail.html', {'event': event})