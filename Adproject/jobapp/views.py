from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def kanpur_jobs_views(request):
    s = '<h1>Kanpur jobs information you can find here.</h1>'
    return HttpResponse(s)


def noida_jobs_views(request):
    s = '<h1>Noida jobs information you can find here.</h1>'
    return HttpResponse(s)


def gurgaon_jobs_views(request):
    s = "<h1 style='color:blue'>Gurgaon jobs information you can find here.</h1>"
    return HttpResponse(s)
