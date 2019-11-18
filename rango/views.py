from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': "index page"}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'name': 'yuhui'}
    return render(request, 'rango/about.html', context=context_dict)
