from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Gender = request.POST['Gender']
        Address = request.POST['Address']
        City = request.POST['City']
        Mobile = request.POST['Mobile']
        Email_id = request.POST['Email']
        password = request.POST['password']

        # Create a new UserProfile instance and save it to the database
        userdetail = UserDetails(
            Name=Name,
            Gender=Gender,
            Address=Address,
            City=City,
            Mobile=Mobile,
            Email_id=Email_id,
            password=password
        )
        userdetail.save()

        # Optionally, you can also use Django's built-in authentication system to handle user accounts and passwords.

        messages.success(request, 'Registration successful.')
        return redirect('register')  # Redirect to the login page after successful registration
    else:
        return render(request, 'account/register.html')  # Render the registration form template for GET requests




# Create your Login functionality here.
def login(request):
    if request.method == 'POST':
        Email_id = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(Email_id=Email_id)
            if user.password == password:
                # Password is correct, log the user in
                auth.login(request, user)
                
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('login')
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'account/login.html')
        

# logout function
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'you are logged out')
    return redirect('login')



@login_required(login_url = 'login')
def dashboard(request):
    return render(request, 'store/dashboard.html')