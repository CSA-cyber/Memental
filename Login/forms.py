from django import forms

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class patient_create_form(forms.Form):
    name = forms.CharField(label='First Name')
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'placeholder': 'example@email.com'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Re Enter Password', widget=forms.PasswordInput())
    age = forms.DateField(
        label="Birthdate", widget=forms.TextInput(attrs={'type': 'date'}))
    phone = forms.CharField(label="Phone no")
    address = forms.CharField(label="Address")


class login_form(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(
        attrs={'placeholder': 'example@email.com'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput())