from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q

def product_list(request):
    products = Product.objects.all()
    categories = Product.objects.values_list('Category', flat=True).distinct()
    product_count = products.count()
    

     # Check if the 'category' query parameter is present in the URL
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(Category=category_filter)
        product_count = products.count()

    context = {
        'products': products,
        'categories': categories,
        'product_count': product_count,
    }
    return render(request, 'store/product.html', context)


def product_detail(request, pid):
    product = get_object_or_404(Product, P_id=pid)  # Retrieve the product or return a 404 if not found
    return render(request, 'store/product_detail.html', {'product': product})


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('P_id').filter(Q(Category__icontains=keyword) | Q(P_name__icontains=keyword))
            product_count = products.count()
    context ={
          'products': products,
          'product_count': product_count,
    }
    return render(request, 'store/product.html', context)