"""medicare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('registration.urls')),
    
    path('product/', include('product.urls')),
    path('product_detail.html', views.product_detail, name='product_detail'),
    path('cart/', include('cart.urls')),
    path('cart/payment.html', views.payment, name='payment'),
    path('order.html', views.order, name='order'),
    path('', include('feedback.urls')),
    path('dashboard.html', views.dashboard, name='dashboard')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)