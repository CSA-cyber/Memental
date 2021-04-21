from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    patient = ""
    if request.user.is_authenticated:
        email = request.user.email

    return render(request, 'index.html', {'patient': patient})


def show_doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctors.html', context)

def doctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    context = {'doctor': doctor}
    return render(request, 'doctor.html', context)
