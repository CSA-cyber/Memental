# from django.db import models
# from django.core.validators import MinLengthValidator, MinValueValidator
# from django.contrib.auth.models import User
# from django.utils import timezone


# class User(models.Model):
#     """A class to generate a user
#     ...

#     Attributes
#     ----------
#     name: models.charfield / str
#         name of the customer
#     address: Location
#         location of a customer
#     phone: int
#         phone number of a customer
#     email: models.EmailField
#         email of a customer
#     password: model
#     """
#     is_doctor = models.BooleanField(default=False)
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#     password = models.CharField(max_length=50, validators=[
#                                 MinLengthValidator(8)])
#     age = models.PositiveIntegerField()
#     phone = models.CharField(max_length=15,
#                              validators=[MinLengthValidator(8)], blank=True, null=True)
#     credit_info = models.CharField(max_length=12,
#                                    validators=[MinLengthValidator(12)], blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     fees = models.FloatField(validators=[MinValueValidator(1)])
#     qualifications = models.TextField()
#     availability = models.BooleanField(default=False)
#     desc = models.TextField()
#     specilization = models.CharField(max_length=255)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def __str__(self):
#         return self.name


# class Appointment(models.Model):
#     patient = models.ForeignKey(
#         'User', on_delete=models.SET_NULL, null=True)
#     doctor = models.ForeignKey(
#         'User', on_delete=models.SET_NULL, null=True)
#     prescription = models.TextField()
#     disease_details = models.CharField(max_length=255)
#     date = models.DateTimeField(default=timezone.now)
#     approval = models.BooleanField(default=False)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def __str__(self):
#         return f'Product:{str(self.product)}\tCustomer: {str(self.customers)}'


# class UserMessage(models.Model):
#     user = models.ForeignKey(
#         'User', on_delete=models.SET_NULL, null=True)
#     doctor = models.ForeignKey(
#         'User', on_delete=models.SET_NULL, null=True)
#     query = models.TextField(default=' ', null=True)
#     reply = models.TextField(default=' ', null=True)
#     date = models.DateTimeField(default=timezone.now)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def __str__(self):
#         return self.user.name
