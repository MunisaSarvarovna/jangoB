from django.http import HttpResponse
from .models import Task
from django.shortcuts import render

# Create your views here.


def week(request, day):
    daily_task =Task.objects.get(day=day)
    return HttpResponse( {daily_task.task} )

def home(request):
    html =""""
    <p><a href=' http://127.0.0.1:8000/table/monday'>monday<Dushanba<p/>
    <p><a href=' http://127.0.0.1:8000/table/monday'>tuesday<seshanba<p/>

    """
    return HttpResponse(html)
