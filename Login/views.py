from django.shortcuts import render

# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def create_account(request):
    return render(request, 'signup.html')

