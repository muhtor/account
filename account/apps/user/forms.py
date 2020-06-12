from django import forms
from .models import User, UserProfile


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={"placeholder": "Email"}),
            'password': forms.TextInput(attrs={"type": "password", "placeholder": "Password"}),
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={"placeholder": "Email"}),
            'password': forms.TextInput(attrs={"type": "password", "placeholder": "Password"}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'country', 'city', 'phone']
        exclude = ['user', 'password']
        widgets = {
            'email': forms.TextInput(attrs={"placeholder": "Email"}),
            'password': forms.TextInput(attrs={"type": "password", "placeholder": "Password"}),
        }