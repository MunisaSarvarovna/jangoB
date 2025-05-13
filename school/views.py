from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def salom(request):
    return HttpResponse("assalomu alekum hush kelibsiz")


def class_info(request):
    return HttpResponse("schoolda 20 ta oquchi bor")