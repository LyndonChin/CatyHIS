from django.http import HttpResponse
from django.shortcuts import render


__author__ = 'liangfei'


def home(request):
    return render(request, 'base.html')
