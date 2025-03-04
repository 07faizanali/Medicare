from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.db.models import Q
from prescription.models import Prescription
from django.contrib.auth.decorators import login_required 

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




  # Add the login_required decorator to ensure the user is authenticated
def product_detail(request, pid):
    product = get_object_or_404(Product, P_id=pid)

    # Check if the product category is "medicine"
    if product.Category == "medicine":
        # Check if the user has already uploaded a prescription
        prescription_exists = Prescription.objects.filter(Email_id=request.user.Email_id).exists()
        if not prescription_exists:
            # Redirect the user to upload a prescription
            return redirect('prescription')

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


    