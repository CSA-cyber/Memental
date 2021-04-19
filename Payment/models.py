from django.db import models
from django.utils import timezone


# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(
        'Hospital.Patient', verbose_name='patient', related_name='appointments', on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(
        'Hospital.Doctor', verbose_name='doctor', related_name='appointments',on_delete=models.SET_NULL, null=True)
    prescription = models.TextField(blank=True, null=True)
    disease_details = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    choices = [
        (-1, 'Waiting doctors approval'),
        (0, 'Denied'),
        (1, 'Approved'),
    ]
    approval = models.IntegerField(choices=choices, default=-1)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.id)
