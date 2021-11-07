
from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from .models import Event
from .forms import EventForm

def index(request):
    all_event = Event.objects.all()
    return render(request, 'event/event_main.html', {'all_event':all_event})

def registration(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('event:index') # 행사 등록 후 쓰고 달력으로 돌아감
        else:
            print(event_form)
    return render(request,'event/event_reg.html',{'event_form':EventForm()})