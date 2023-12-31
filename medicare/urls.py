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
    path('prescription/', include('prescription.urls')),
    path('cart/', include('cart.urls')),
    path('', include('feedback.urls')),
    path('', include('payment.urls')),
    path('', include('order.urls')),
    path('store/dashboard.html', views.dashboard, name='dashboard'),
    path('about_us/', views.about_us, name="about_us"),
    path('contact_us/', views.contact_us, name="contact_us"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
