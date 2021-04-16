from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required


def payment(request):
    return render(request, 'payment.html')


# @login_required
def approval_status(request):
    return render(request, 'status.html')


def make_appointment(request):
    context = {}
    return render(request, 'appointment.html', context)

def appointment_views(request):
    return render(request, 'appointment.html')


def checkout(request):
    return render(request, 'checkout.html')
