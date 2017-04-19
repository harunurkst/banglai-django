from django.shortcuts import render
from .models import Districts, Divisions



def district_list(request):
    div = Divisions.objects.get(name='Khulna')
    districts = Districts.objects.filter(division=div)
    context = {
        'districts': districts,
    }
    return render(request, 'information/districts.html', context)
