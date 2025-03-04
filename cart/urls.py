from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    
    path('add_cart/<int:P_id>/', views.add_cart, name='add_cart'),
    path('increment_cart/<int:cart_id>/', views.increment_cart, name='increment_cart'),
    path('decrement_cart/<int:cart_id>/', views.decrement_cart, name='decrement_cart'),
    path('remove_item_from_cart/<int:cart_id>/', views.remove_item_from_cart, name='remove_item_from_cart'),

    
]

