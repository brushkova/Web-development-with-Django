from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    if request.GET.get('name'):
        message = 'Your name: %r' % request.GET['name']
    else:
        message = 'Your name nothing!'
    return HttpResponse(message)

    # name = request.GET.get("name", "world")
    # return HttpResponse("Hello, {}!".format(name))
