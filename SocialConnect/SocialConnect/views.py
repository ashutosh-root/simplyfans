from django.shortcuts import render
from django.conf import settings

def home_view(request):
    STATIC_URL = settings.STATIC_URL
    return render(request, "home.html", locals())