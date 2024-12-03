from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages


from .forms import UserPreferencesForm
from .models import UserPreferences
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views  # Ensure this line is included

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
            return redirect('home')  # Stay on login page after logging in for now
        else:
            # Invalid credentials, show error and redirect to signup
            messages.error(request, 'Invalid credentials.')
            return redirect('signup')  # Redirect to signup page

    return render(request, 'users/login.html')  # Ensure login page renders




# View to render the home page
# def home(request):
#     return render(request, 'users/home.html')


#View to render the home page and logic
# def home(request):
#     if request.method == 'POST':
#         form = UserPreferencesForm(request.POST, instance=request.user.userpreferences)
#         if form.is_valid():
#             preferences = form.save(commit=False)
#             preferences.user = request.user
#             preferences.save()
#             # Redirect to a success page or refresh
#             return redirect('home')
#     else:
#         form = UserPreferencesForm(instance=request.user.userpreferences)

#     return render(request, 'users/home.html', {'form': form})

# @login_required
# def home(request):
#     # Check if the user has preferences, create a new one if not
#     preferences, created = UserPreferences.objects.get_or_create(user=request.user)

#     if request.method == 'POST':
#         form = UserPreferencesForm(request.POST, instance=preferences)  # Update preferences
#         if form.is_valid():
#             form.save()  # Save the preferences
#             return redirect('home')  # Redirect to the home page or wherever you want
#     else:
#         form = UserPreferencesForm(instance=preferences)  # Load existing preferences into the form

#     return render(request, 'users/home.html', {'form': form})

# def home_view(request):
#     if request.method == 'POST':
#         # If the user is submitting preferences
#         kanji_count = request.POST.get('number_of_kanjis')
#         duration = request.POST.get('email_duration')
#         email_time = request.POST.get('email_time')  # Ensure this is being captured from the form
        
#         if email_time:
#             preferences = UserPreferences.objects.create(
#                 user=request.user,
#                 number_of_kanjis_per_day=kanji_count,
#                 email_duration=duration,
#                 email_time=email_time  # Ensure email_time is saved
#             )
#             preferences.save()
#         else:
#             messages.error(request, 'Please select an email time')
#     else:
#         # Handle GET requests
#         preferences = UserPreferences.objects.filter(user=request.user).first()
        
#         # If no preferences exist yet, initialize with defaults or redirect to form
#         if not preferences:
#             return redirect('preferences')  # Or render a default form for preferences

#     return render(request, 'home.html', {'preferences': preferences})


@login_required
def home(request):
    # Get or create preferences for the logged-in user
    preferences, created = UserPreferences.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Get the selected values from the form
        kanji_per_day = request.POST.get('kanji_per_day')
        duration_in_days = request.POST.get('duration_in_days')
        email_time = request.POST.get('email_time')

        # Update preferences if data is valid
        preferences.kanji_per_day = kanji_per_day
        preferences.duration_in_days = duration_in_days
        preferences.email_time = email_time

        # Save updated preferences
        preferences.save()

        # Optionally, you can redirect after saving
        return redirect('home')  # Redirect to avoid re-submitting the form if refreshed

    return render(request, 'users/home.html', {'form': preferences})




# This is for user preferences data 

def preferences_view(request):
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST)
        if form.is_valid():
            preferences = form.save(commit=False)
            preferences.user = request.user  # Associate preferences with the logged-in user
            preferences.save()
            # You can call your save_preferences function here if needed
            return redirect('home')  # Redirect to the home page or wherever you want
    else:
        form = UserPreferencesForm()

    return render(request, 'path/to/preferences_template.html', {'form': form})


# Custom login view
class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'  # Specify your actual login template path here


























