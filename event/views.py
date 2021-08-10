
from django.shortcuts import render

def index(request):
    return render(request, 'event/event_test.html')

