from django.shortcuts import render
from .models import Travel


# Create your views here.
def travel(request):
    travel_tips = Travel.objects.all()
    return render(request, 'travel.html', {'travel_tips': travel_tips})