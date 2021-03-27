from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(UserMessage)
