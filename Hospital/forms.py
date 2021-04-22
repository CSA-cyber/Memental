from datetime import date
from django import forms
from django.conf import settings


# from django.forms import widgets
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class create_appointment(forms.Form):
    # appointment_date = forms.DateField(
    #     label="Appointment Date", input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(attrs={'class': 'form-control picker-input'}, years=[date.today().year]))
    appointment_date = forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(years=[date.today().year]))
    appointment_time = forms.TimeField(widget=forms.TimeInput({'class': 'form-control td-input', 'type': 'time', 'placeholder': 'time'}))
    
    
    
class login_form(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': 'example@email.com'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': 'Password'}))
