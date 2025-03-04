from django.shortcuts import render, redirect
from registration.models import UserDetails
from .models import Prescription  # Import your UserProfile model
from django.contrib import messages  # Import messages for displaying flash messages


# Create your views here.
def prescriptions(request):
    if request.method == 'POST':
        Email_id = request.POST['Email_id']
        pres_image = request.POST['image']
        

        
        # Retrieve the UserDetail instance based on the provided email
        try:
            user_detail = UserDetails.objects.get(Email_id=Email_id)
        except UserDetails.DoesNotExist:
            # Handle the case where the UserDetail instance doesn't exist
            messages.error(request, 'User with this email does not exist.')
            return redirect('prescription_list')  # Redirect back to the feedback page

      
       # Create a new UserProfile instance and save it to the database
        prescriptions = Prescription(
            Email_id=user_detail,
            pres_image=pres_image,
            
            
        )
        prescriptions.save()
        
    return render(request, 'store/upload_prescription.html')

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    context = {
        'prescriptions': prescriptions,
    }
    return render(request, 'store/prescription_list.html', context)