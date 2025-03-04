from .models import AddToCart

def cart_count(request):
    cart_count = 0
    
    if request.user.is_authenticated:
        cart_count = AddToCart.objects.filter(email_id__Email_id=request.user.Email_id).count()
    
    return {'cart_count': cart_count}
