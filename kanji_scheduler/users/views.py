from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken.')
            else:
                user = User.objects.create_user(username=email, email=email, password=password1)
                messages.success(request, 'Account created successfully!')
                return redirect('login')  # Redirect to login after successful signup
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'users/signup.html')  # This renders both forms for simplicity

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('login')  # Stay on login page after logging in for now
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'users/login.html')  # Ensure login page renders


# View to render the home page
def home(request):
    return render(request, 'users/home.html')

# # Home view
# def home_view(request):
#     return render(request, 'users/home.html')  





# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth.models import User
# from django.contrib import messages

# # Login view
# def login_view(request):
#     # Always log out the user before rendering the login page
#     if request.user.is_authenticated:
#         auth_logout(request)  # Log the user out to ensure a fresh login attempt

#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)  # Log the user in
#             return redirect('home')    # Redirect to home after successful login
#         else:
#             messages.error(request, 'Invalid credentials. Please try again.')

#     return render(request, 'users/signup.html')  # Show the login/signup form



# # Signup view
# def signup_view(request):
#     # If user is already logged in, redirect to home
#     if request.user.is_authenticated:
#         return redirect('home')  

#     # Handle signup form submission
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, 'Email already taken.')
#             else:
#                 user = User.objects.create_user(username=email, email=email, password=password1)
#                 auth_login(request, user)  # Automatically log the user in after signup
#                 return redirect('home')    # Redirect to home after successful signup
#         else:
#             messages.error(request, 'Passwords do not match. Please try again.')

#     return render(request, 'users/signup.html')


# # Home view
# def home_view(request):
#     # Only allow logged-in users to access the home page
#     if not request.user.is_authenticated:
#         return redirect('login')  # Redirect to login page if user is not logged in

#     return render(request, 'users/home.html')

# # Optional: Logout view to clear the session and log out
# def logout_view(request):
#     auth_logout(request)
#     return redirect('login')


# def redirect_to_login(request):
#     return redirect('login')  # Redirect to login page when accessing '/'



# from django.shortcuts import render
# from django.contrib.auth import authenticate, login as auth_login
# from django.contrib.auth.models import User
# from django.contrib import messages

# # Signup view to display the signup form
# def signup_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.error(request, 'Email already taken.')
#             else:
#                 user = User.objects.create_user(username=email, email=email, password=password1)
#                 messages.success(request, 'Account created successfully!')
#                 return render(request, 'users/signup.html')  # Stay on signup page after successful signup
#         else:
#             messages.error(request, 'Passwords do not match.')
    
#     return render(request, 'users/signup.html')  # Renders the signup page

# # Login view to display the login form
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)
#             return render(request, 'users/home.html')  # Redirect to home after login
#         else:
#             messages.error(request, 'Invalid credentials.')

#     return render(request, 'users/signup.html')  # Renders the signup page if login fails

# # Home view to display the home page
# def home_view(request):
#     return render(request, 'users/home.html')  # Renders the home page
