from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
