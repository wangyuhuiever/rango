from django.http import HttpResponse


def index(request):
    return HttpResponse('balabalabala<br/><a href="/rango/about/">about page</a>')


def about(request):
    return HttpResponse('about page<br/><a href="/rango/">index page</a>')