from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('pay/', views.payment, name='payment'),
    path('status/', views.approval_status, name='status'),
    path('booking-page/', views.make_appointment, name='booking-page'),
    path('update_appointment/', views.update_appointment, name='update_appointment')
]