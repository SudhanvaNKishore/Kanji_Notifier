from django import forms
from .models import UserPreferences

class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['kanji_per_day', 'duration_in_days', 'email_time', 'subscribed']
