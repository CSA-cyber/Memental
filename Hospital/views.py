from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    context = {}
    return render(request, 'hospital.html', context)





def show_doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)