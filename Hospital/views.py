from django.shortcuts import redirect, render
from .models import *
from datetime import datetime
from .forms import *
from django.template import RequestContext
from Payment.models import Appointment

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
    form = CreateAppointment()

    context = {'doctor': doctor,
               'form': form}

    return render(request, 'doctor.html', context)


def show_profile(request):
    if request.user.is_authenticated:
        user = request.user
        patient = Patient.objects.filter(user=user).first()
        if patient:
            form = UpdateInfo()
            form.fields['phone'].widget.attrs['value'] = patient.phone
            form.fields['credit_card'].widget.attrs['value'] = patient.credit_info
            form.fields['address'].widget.attrs['value'] = patient.address

            if request.method == 'POST':
                form = UpdateInfo(request.POST)
                if form.is_valid():
                    patient.phone = form.cleaned_data['phone']
                    patient.address = form.cleaned_data['address']
                    patient.credit_info = form.cleaned_data['credit_card']

                    password0 = form.cleaned_data['password0']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']

                    if password0 and password0 == patient.password:
                        if password1 and password1 == password2:
                            patient.password = password1
                            request.user.set_password(password1)
                            request.user.save()

                    patient.save()

            appointments = Appointment.objects.filter(
                patient=patient)
            return render(request, 'profile.html', {'appointments': appointments, 'patient': patient, 'form': form})
        else:
            doctor = Doctor.objects.get(user=user)
            form = UpdateDoctorForm()
            approve_form = ApproveForm()
            
            form.fields['phone'].widget.attrs['value'] = doctor.phone
            form.fields['credit_card'].widget.attrs['value'] = doctor.credit_info
            form.fields['address'].widget.attrs['value'] = doctor.address
            form.fields['fees'].widget.attrs['value'] = doctor.fees
            form.fields['qualifications'].initial = doctor.qualifications
            form.fields['desc'].initial = doctor.desc
            form.fields['education'].initial = doctor.education
            form.fields['availability'].initial = doctor.availability
            form.fields['specilization'].initial = doctor.specilization
            appointments = Appointment.objects.filter(doctor=doctor)
            
            approve_form.fields['approval'].initial = doctor.specilization
            
            

            if request.method == 'POST':
                form = UpdateDoctorForm(request.POST)
                approve_form = ApproveForm(request.POST)
                if form.is_valid():
                    doctor.phone = form.cleaned_data['phone']
                    doctor.address = form.cleaned_data['address']
                    doctor.credit_info = form.cleaned_data['credit_card']

                    password0 = form.cleaned_data['password0']
                    password1 = form.cleaned_data['password1']
                    password2 = form.cleaned_data['password2']

                    if password0 and password0 == doctor.password:
                        if password1 and password1 == password2:
                            doctor.password = password1
                            request.user.set_password(password1)
                            request.user.save()

                    doctor.fees = form.cleaned_data['fees']
                    doctor.qualifications = form.cleaned_data['qualifications']
                    doctor.desc = form.cleaned_data['desc']
                    doctor.education = form.cleaned_data['education']
                    doctor.availability = form.cleaned_data['availability']
                    doctor.specilization = form.cleaned_data['specilization']
                    doctor.save()
                    
                elif approve_form.is_valid():
                    approval = approve_form.cleaned_data['approval']
                    approval = int(approval)
                    appointment_id = request.POST['appointment_id']
                    appointment_id = int(appointment_id)
                    print(f'id: {appointment_id} choice: {approval}')
                    appointment = Appointment.objects.get(id=appointment_id)
                    appointment.approval = approval
                    appointment.save()

            return render(request, 'profile_doctor.html', {'doctor': doctor, 'appointments': appointments, 'form': form, 'approve_form':approve_form})
    else:
        return redirect('login')


def show_emergency(request):
    cabins = Emergency_Cabin.objects.all()
    return render(request, 'emergency.html', {'cabins': cabins})
