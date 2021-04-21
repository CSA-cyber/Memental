from django import forms
from django.conf import settings
from datetime import date
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class patient_create_form(forms.Form):
    fname = forms.CharField(label='First Name', widget=forms.TextInput(attrs={
                            'name': "first_name", 'id': "first_name", 'class': "input-text", 'placeholder': "First Name"}))
    lname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
                            'name': "last_name", 'id': "last_name", 'class': "input-text", 'placeholder': "Last Name"}))

    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
                             'name': "company", 'class': "company", 'id': "company", 'placeholder': "Email"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'name': "company", 'class': "company", 'id': "company", 'placeholder': 'Password'}))
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'name': "company", 'class': "company", 'id': "company", 'placeholder': 'Re-Enter Password'}))

    bdate = forms.DateField(
        label="Birthdate", input_formats=settings.DATE_INPUT_FORMATS, widget=forms.SelectDateWidget(attrs={'class': 'form-date'}, years=[*range(date.today().year)][::-1]))
    # bdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, widget=forms.DateInput)
    phone = forms.CharField(label="Phone no", widget=forms.TextInput(attrs={
                            'name': "phone", 'class': 'phone', 'id': "phone", 'placeholder': "Phone Number"}))
    address = forms.CharField(label="Address")


class login_form(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': 'example@email.com'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': 'Password'}))
