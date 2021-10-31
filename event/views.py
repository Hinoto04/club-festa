
from django.shortcuts import render

from django.shortcuts import render,redirect,get_object_or_404
from .models import Event
from .forms import EventForm

def index(request):
    return render(request, 'event/event_main.html')

def registration(request):
    if request.method == "REG":
        event_form = EventForm(request.REG)
        if event_form.is_valid():
            event_form.save()
            return redirect('index') # 행사 등록 후 쓰고 달력으로 돌아감
    else:
        event_form = EventForm()
    return render(request,'event/event_reg.html',{'event_form':event_form})