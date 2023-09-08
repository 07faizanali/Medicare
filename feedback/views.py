from django.shortcuts import render, redirect
from registration.models import UserDetails
from .models import Feedback  # Import your UserProfile model
from django.contrib import messages  # Import messages for displaying flash messages


# Create your views here.
def feedback(request):
    if request.method == 'POST':
        Email_id = request.POST['Email_id']
        Services = request.POST['Services']
        Comment = request.POST['Comment']

        
        # Retrieve the UserDetail instance based on the provided email
        try:
            user_detail = UserDetails.objects.get(Email_id=Email_id)
        except UserDetails.DoesNotExist:
            # Handle the case where the UserDetail instance doesn't exist
            messages.error(request, 'User with this email does not exist.')
            return redirect('feedback')  # Redirect back to the feedback page

      
       # Create a new UserProfile instance and save it to the database
        feedbacks = Feedback(
            Email_id=user_detail,
            Services=Services,
            Comment=Comment,
            
        )
        feedbacks.save()
        return render(request, 'feedback/success.html')
    return render(request, 'feedback/feedback.html')