from .models import Appointment
from Hospital.models import Doctor, Patient
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.formats import localize
import json
# Create your views here.

# @login_required


def payment(request):
    return render(request, 'payment.html')


# @login_required
def approval_status(request):
    return render(request, 'status.html')


def make_appointment(request):
    if request.user.is_authenticated:
        patient = request.user.patient
        doctor = Doctor.objects.get(id=1)
        appointment, created = Appointment.objects.get_or_create(
            patient=patient, doctor=doctor, disease_details='Fine')
    else:
        return appointment_views(request)
        # return render(request, 'login.html')

    context = {'appointment': appointment}
    return render(request, 'appointment.html', context)


def appointment_views(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments, 'amount': len(appointments)}
    return render(request, 'appointment.html', context)


def checkout(request):
    if request.user.is_authenticated:
        patient = request.user.patient
        doctor = Doctor.objects.get(id=1)
        appointment, created = Appointment.objects.get_or_create(
            patient=patient, doctor=doctor, disease_details='Fine')
    else:
        appointment = Appointment.objects.get(id=10)
        time = appointment.date
        time = localize(time)
        # import inspect
        # attrs = inspect.getmembers(time, lambda a:not(inspect.isroutine(a)))
        # print(attrs)
        context = {'appointment': appointment, 'time': time}
        
    return render(request, 'checkout.html', context)

def update_appointment(request):
    data = json.loads(request.body)
    doctorId = data['doctorId']
    action = data['action']
    
    print('Acrion:', action)
    print('DoctorId:', doctorId)
    
    patient = request.user.patient
    doctor = Doctor.objects.get(id=doctorId)
    
    appointment, created = Appointment.objects.get_or_create(
            patient=patient, doctor=doctor, disease_details='Fine')
    appointment.save()
    return JsonResponse('Appointment was added', safe=False)