from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.show_doctors, name='doctors'),
    path('doctor/<str:pk>/', views.doctor, name='doctor')
]