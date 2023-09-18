from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<int:P_id>/', views.add_cart, name='add_cart'),
    
    path('remove/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

