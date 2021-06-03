from django.http.response import HttpResponse
from django.shortcuts import render


def noname(request):
    return HttpResponse('Check this page')
