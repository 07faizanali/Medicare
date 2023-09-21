from django.urls import path
from . import views

urlpatterns = [
    path('', views.prescriptions, name='prescription'),
    path('prescription_list/', views.prescription_list, name='prescription_list'),
]