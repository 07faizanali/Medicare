from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product'),
    path('product/<int:pid>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
]
