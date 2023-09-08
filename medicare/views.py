from django.shortcuts import render
from product.models import Product
def home(request):
    products=Product.objects.all()

    context = {
        'products': products,
    }
    return render(request,'home.html', context)

def dashboard(request):
    return render(request,'dashboard.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def product(request):
    return render(request,'product.html')

def product_detail(request):
    return render(request,'product_detail.html')

def cart(request):
    return render(request,'cart.html')

def payment(request):
    return render(request,'payment.html')

def order(request):
    return render(request,'order.html')

def feedback(request):
    return render(request,'feedback.html')