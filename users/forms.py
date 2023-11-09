from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CusRatingFeedback

class RegistrationForm(UserCreationForm):
    email = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class CusRatFeedform(forms.ModelForm):
    class Meta:
        model = CusRatingFeedback
        fields = ['ratings', 'feedback', 'user_type']

