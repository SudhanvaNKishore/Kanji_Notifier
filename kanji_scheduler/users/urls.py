from django.urls import path
from . import views
from .views import signup_view, login_view, home, preferences_view, CustomLoginView 

urlpatterns = [
    # path('login/', views.login_view, name='login'),  # Login page URL
    path('login/', CustomLoginView.as_view(), name='login'),  # Use the custom login view here
    path('signup/', views.signup_view, name='signup'),  # Signup page URL

    path('home/', views.home, name='home'),


    path('preferences/', views.preferences_view, name='preferences'),
]
