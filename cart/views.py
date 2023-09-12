from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from product.models import Product
from .models import AddToCart

def _cart_id(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart_id = hash(request.session.session_key)
        request.session['cart_id'] = cart_id
    return cart_id

@login_required
def add_cart(request, P_id):
    try:
        product = get_object_or_404(Product,P_id=P_id)   # get the product
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")
    cart_id = _cart_id(request)
    try:
        cart = AddToCart.objects.get(cart_id=cart_id)
    except AddToCart.DoesNotExist:
        cart = AddToCart.objects.create(cart_id=cart_id)
        cart.save()

    try:
        # Set the 'p_id' field with the 'product' object
        cart_item, created = AddToCart.objects.get_or_create(
            p_id=product,  # Set 'p_id' with the 'product' object
            cart=cart,
            defaults={
                'email_id': request.user.UserDetails.Email_id,
                'p_name': product.P_name,
                'price': product.Price,
                'p_image': product.P_image.url,
                'p_quantity': 1,
            }
        )

        if not created:
            cart_item.p_quantity += 1
            cart_item.save()

        return redirect('cart')

    except Exception as e:
        print(e)  # Print any exceptions for debugging purposes

    return redirect('cart')

def cart(request):
    return render(request, 'store/cart.html')