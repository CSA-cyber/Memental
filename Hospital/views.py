from django.shortcuts import redirect, render
from .models import *
from datetime import datetime
from .forms import *
from django.template import RequestContext
import Payment
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
    context = {}
    form = create_appointment()
    
    # if request.method == 'POST':
    #     print('true')
    #     form = create_appointment(request.POST)
        
    #     if not request.user.is_authenticated:
    #         return redirect('login')
        
    #     if form.is_valid():
    #         print(datetime.now())
    #         appointment_date = form.cleaned_data['appointment_date']
    #         appointment_time = form.cleaned_data['appointment_time']
    #         context = {'doctor_id': pk, 'appointment_time': appointment_time}
    #         return render(request, 'boooking_page.html', context)
            
    context = {'doctor': doctor,
               'form': form}
    
    return render(request, 'doctor.html', context)

def showProfile(request):
    if request.user.is_authenticated:
        usr = User.objects.get(email=request.user.username)
        email = request.user.username
        patient_id = Patient.objects.get(email=email).id
        appointments = Payment.models.Appointment.objects.filter(patient_id=patient_id)
        return render(request, 'profile.html', {'usr':usr,'appointments':appointments})
    else:
        return redirect('login')
        
def show_emergency(request):
    cabins = Emergency_Cabin.objects.all()
    return render(request, 'emergency.html', {'cabins':cabins})