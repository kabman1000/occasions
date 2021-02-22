from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.

def index(request):
    day_today = datetime.datetime.now()
    return render(request, 'independence/index.html', {'day_today': day_today.month == 3 and day_today.day == 6 })