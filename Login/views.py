from Hospital.models import Patient
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from datetime import date
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
# Create your views here.


def login_user(request):
    form = login_form()
    context = {}
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:                    
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('admin:index'))
                return redirect('index')
            else:
                messages.info(request, 'Email and password did not match')
                return redirect('login')

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'user logged out')
    return render(request, 'index.html')


def create_account(request):
    form = patient_create_form()

    if request.method == 'POST':
        form = patient_create_form(request.POST)

        def calculate_age(born):
            today = date.today()
            return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            if Patient.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('doctors')

            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            age = form.cleaned_data['age']
            age = calculate_age(age)
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            user = User.objects.create_user(email, email, password1)
            # user.save()
            patient = Patient.objects.create(
                user=user, name=name, email=email, password=password1, age=age, phone=phone, address=address)
            # patient.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'signup.html', context)
