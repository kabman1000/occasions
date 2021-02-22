from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    repub_day = datetime.datetime.now()
    context = {'repub_day': repub_day.month == 7 and repub_day.day == 1 }
    return render(request, 'republic/index.html', context)
