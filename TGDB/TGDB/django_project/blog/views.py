from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import datetime


def index(request):
    return HttpResponse("Hello Django")


def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {'now': now, "template_name": 'blog/nav.html',
                                                  'base_dir': settings.BASE_DIR})
