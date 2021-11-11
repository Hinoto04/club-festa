
from time import strftime
from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Event
from .forms import EventForm

from datetime import date, datetime, timedelta, tzinfo, time, timezone as tz
import numpy as np

def index(request, event_month=None):
    class day():
        
        def __init__(self, date):
            self.date = date
            self.event = []
        
        def __str__(self):
            return self.event
        
        def __repr__(self):
            return str(self.event)
    
    #대충 첫 날짜
    if event_month:
        startdate = datetime.strptime(str(event_month),'%Y%m')
    else:
        today = timezone.localtime()
        startdate = date(year = today.year, month = today.month, day=1)
    
    mt = (startdate.weekday()+1)%7 # 월요일==0+1 .... 일요일==6+1
    year_month = startdate.strftime("%Y-%m")
    startdate = startdate - timedelta(days = mt)  #달력의 공칸 만큼 시작일 연기()
    
    sd = datetime.combine(startdate, time(), tz(timedelta(hours=9)))
    events = Event.objects.filter(start_date__gte=sd).filter(end_date__lte=sd+timedelta(days=35)).order_by('start_date')
    
    month = []
    for i in range(35):
        month.append(day(startdate + timedelta(days = i)))
    for event in events:
        for d in month:
            if event.start_date <= d.date <= event.end_date:
                d.event.append(event)
            if d.date == event.end_date:
                break
    month = np.reshape(month, (5,7))
    #    날짜 확인 후 해당 날짜에 event 추가
    #    기간제인 경우 해당 기간의 모든 날짜에 event 추가
    
    context = {
        'year_month': year_month, 
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