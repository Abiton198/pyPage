from django.shortcuts import render
from .models import About
# Create your views here.


def about(request):
    about_us = About.objects.all()
    return render(request, 'about.html', {'about': about_us})