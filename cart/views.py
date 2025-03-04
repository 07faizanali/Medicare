from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AddToCart
from product.models import Product  # Import your Product model here
from registration.models import UserDetails
from django.contrib import messages

@login_required
def add_cart(request, P_id):
    # Retrieve the user from the request, assuming user is available in the request.
    email_id = request.user.Email_id

    try:
        # Fetch product information based on P_id from your Product model
        product = Product.objects.get(pk=P_id)
        P_name = product.P_name  # Replace 'name' with the actual field name for product name.
        P_price = product.Price  # Replace 'price' with the actual field name for product price.
        P_image = product.P_image  # Replace 'image_url' with the actual field name for product image URL.

        P_quantity = 1  # You can set the default quantity as needed.
        user_details = get_object_or_404(UserDetails, Email_id=email_id)
          
     # Check if the same product is already in the cart

        try:
            cart_item = AddToCart.objects.get(email_id=user_details, p_id=product)
            cart_item.p_quantity += P_quantity
            cart_item.price += P_price * P_quantity   # update total price
            cart_item.save()
        except AddToCart.DoesNotExist:
            cart_item = AddToCart(
                email_id=user_details,
                p_id=product,
                p_name=P_name,
                price=P_price * P_quantity, # Initialize with the total price
                p_image=P_image,
                p_quantity=P_quantity,
            )
            cart_item.save()

             # Redirect back to the cart page after adding the product
        return redirect('cart')

    except Product.DoesNotExist:
        # Handle the case where the product with the given P_id does not exist.
        pass


@login_required
def increment_cart(request, cart_id):
    
        # Get the cart item to update
        cart_item = AddToCart.objects.get(pk=cart_id)
        
        if cart_item.p_quantity < 1:
           cart_item.p_quantity +=1
           cart_item.price += cart_item.p_id.Price  # Update the price
           cart_item.save()
           messages.success(request, "Item quantity incremented.")
        else:
            messages.error(request, "You can only update items in your own cart.")
   

        return redirect('cart')



@login_required
def decrement_cart(request,cart_id):
    # Get the cart item to remove
    cart_item = AddToCart.objects.get(pk=cart_id)
        
    if cart_item.p_quantity > 1:
        cart_item.p_quantity -=1
        cart_item.price -= cart_item.p_id.Price  # Update the price
        cart_item.save()
    else:
        cart_item.delete() 
        # Check if the cart item belongs to the logged-in user
    return redirect('cart')

@login_required
def remove_item_from_cart(request,cart_id):
    user_email = request.user.Email_id
    user_cart_items = AddToCart.objects.filter(email_id__Email_id=user_email,cart_id=cart_id)
    
    # Delete all cart items for the user
    user_cart_items.delete()
    return redirect('cart')


# cart_utils.py

def clear_cart(request):
    user_email = request.user.Email_id
    user_cart_items = AddToCart.objects.filter(email_id__Email_id=user_email)
    
    # Delete all cart items for the user
    user_cart_items.delete()


@login_required
def cart(request):
    # Retrieve cart items for the logged-in user
    email_id = request.user.Email_id
    user_cart = AddToCart.objects.filter(email_id__Email_id=email_id)

     # Calculate the total price dynamically
    total_price = sum(cart_item.price for cart_item in user_cart)
   
    tax=(2* total_price)/100
    grand_total= total_price + tax
    context = {
        'carts': user_cart,
        'total_price': total_price,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html' ,context)

    

