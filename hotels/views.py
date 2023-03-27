from django.shortcuts import render
from .models import Hotel
# Create your views here.


def hotels(request):
    hotels_res = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels_res})
