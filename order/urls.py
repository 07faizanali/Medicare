from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('order/', views.order, name='order'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
]
