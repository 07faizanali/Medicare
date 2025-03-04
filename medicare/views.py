from django.shortcuts import render
from product.models import Product
def home(request):
    products=Product.objects.all()

    context = {
        'products': products,
    }
    return render(request,'home.html', context)

def dashboard(request):
    return render(request,'store/dashboard.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def product(request):
    return render(request,'product.html')

def product_detail(request):
    return render(request,'store/product_detail.html')

def about_us(request):
    return render(request, 'includes/about_us.html')

def contact_us(request):
    return render(request, 'includes/contact_us.html')