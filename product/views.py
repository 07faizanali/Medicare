from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Retrieve the product or return a 404 if not found
    return render(request, 'product/product_detail.html', {'product': product})


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(Category__icontains=keyword) | Q(P_name__icontains=keyword))
            product_count = products.count()
    context ={
          'products': products,
          'product_count': product_count,
    }
    return render(request, 'product.html', context)