from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('order/', views.order, name='order'),
]
