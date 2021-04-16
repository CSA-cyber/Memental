from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.payment, name='payment'),
    path('status/', views.approval_status, name='status'),
    path('appointment/', views.make_appointment, name='appointment'),
    path('appointments/', views.appointment_views, name='appointments')
]