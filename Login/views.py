from Hospital.models import Patient
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from datetime import date
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import *
from .forms import *
# Create your views here.


def login_user(request):
    form = login_form()
    
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                auth_login(request, user)
                print('succes')
                patient = Patient.objects.get(email=email)
                return redirect('index')
            else:
                print('not authorized')
                return redirect('signup')
        
    
    context = {'form': form}        
    return render(request, 'login.html', context)


def create_account(request):
    form = patient_create_form()

    if request.method == 'POST':
        form = patient_create_form(request.POST)

        def calculate_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
        if form.is_valid():
            name = form.cleaned_data['fname']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            age = form.cleaned_data['age']
            age = calculate_age(age)
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            patient = Patient.objects.create(name=name, email=email, password=password1, age=age, phone=phone, address=address)
            patient.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)
