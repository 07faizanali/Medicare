from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order  # Import your Order model

@login_required  # Use the login_required decorator to ensure the user is logged in
def order(request):
    # Retrieve the user's orders
    user = request.user  # Assuming you are using Django's built-in user authentication
    orders = Order.objects.filter(email_id=user.Email_id)  # Adjust this based on your model structure

    context = {
        'orders': orders,
    }

    return render(request, 'store/order.html', context)

@login_required
def cancel_order(request,order_id):
    user_email = request.user.Email_id
    user_order_item = Order.objects.filter(email_id__Email_id=user_email,order_id=order_id)
    
    # Delete all cart items for the user
    user_order_item.delete()
    messages.success(request, 'order cancel sucessful')
    return redirect('order')
