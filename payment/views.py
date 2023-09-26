from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Payment
from order.models import Order
from cart.models import AddToCart
from product.models import Product
from django.contrib import messages
from cart.views import clear_cart
from django.utils import timezone

@login_required
def make_payment(request):
    if request.method == 'POST':
        user_details = request.user  # Retrieve the UserDetails instance associated with the current user
        grand_total = float(request.POST.get('grand_total', 0))
        pay_mode = request.POST.get('paymode', '')
        card_no = request.POST.get('card_no', '')
        cvv = request.POST.get('cvv', '')
        exp_month = request.POST.get('month', '')
        exp_year = request.POST.get('year', '')
        h_name = request.POST.get('holder_name', '')

        if not card_no:
            messages.error(request, "Card number is required.")
            return redirect('make_payment')  # Redirect to the payment page or an appropriate URL
        if not exp_year.isdigit():
            messages.error(request, "Invalid expiration year.")
            return redirect('make_payment')  # Redirect to the payment page or an appropriate URL

        # Convert 'exp_year' to an integer
        exp_year = int(exp_year)

        # Retrieve the product IDs from the user's cart
        email_id = request.user.Email_id
        user_cart = AddToCart.objects.filter(email_id__Email_id=email_id)
        product_ids = [cart_item.p_id.pk for cart_item in user_cart]

          # Calculate the total quantity based on items in the cart
        total_quantity = sum(cart_item.p_quantity for cart_item in user_cart)

        # Create a Payment object for each product in the cart
        for product_id in product_ids:
            product = Product.objects.get(pk=product_id)
            payment = Payment(
                
                p_id=product,
                email_id=user_details,  # Use the UserDetails instance
                amount=grand_total,
                pay_mode=pay_mode,
                card_no=card_no,
                cvv=cvv,
                exp_month=exp_month,
                exp_year=exp_year,
                h_name=h_name,
                pay_date=timezone.now(),
            )
            payment.save()

        # Clear the cart after successful payment (assuming you have it implemented)
        clear_cart(request)

        order = Order(
            pay_id=payment,  # Payment object istemal karo
            p_id=product,  # Product ID ko None ya NULL rakho, kyunki product abhi select nahi hua hai
            email_id=user_details,  # UserDetails instance istemal karo
            shipp_address=request.user.Address,  # Shipping address abhi set nahi kiya gaya hai
            quantity=total_quantity,  # Aapko apne cart logic ke hisab se isko adjust kar sakte hain
            amount=grand_total,  # Payment amount istemal karo
            order_date=timezone.now(),
        )
        order.save()

        messages.success(request, 'Payment successful.')
        return redirect('make_payment')  # Redirect to a success page

    # Handle GET request and pass the total price to the template
    email_id = request.user.Email_id
    user_cart = AddToCart.objects.filter(email_id__Email_id=email_id)
    total_price = sum(cart_item.price for cart_item in user_cart)
    tax = (2 * total_price) / 100
    grand_total = total_price + tax

    context = {
        'grand_total': grand_total,
    }
    return render(request, 'store/payment.html', context)


