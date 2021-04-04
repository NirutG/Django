from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def static_media(request):
    return render(request, 'static-media.html')


def static_css(request):
    return render(request, 'static-css.html')


def static_js(request):
    return render(request, 'static-js.html')


def bootstrap(request):
    return render(request, 'bootstrap.html')
