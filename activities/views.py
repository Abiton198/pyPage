from django.shortcuts import render
from .models import Activity


# Create your views here.
def activity(request):
    activities = Activity.objects.all()
    return render(request, 'activities.html', {'activities': activities})