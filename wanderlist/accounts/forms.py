from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Destination, UserProfile
from django_countries import countries
from django_countries.widgets import CountrySelectWidget


# ==============================
# 👤 USER REGISTRATION FORM
# ==============================
class CustomUserCreationForm(UserCreationForm):
    """Form for registering a new user with styled inputs."""
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Re-enter password"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),
        }
        labels = {
            "username": "Username",
            "email": "Email",
        }
        help_texts = {
            "username": None,
        }


# ==============================
# 🔐 USER LOGIN FORM
# ==============================
class CustomAuthenticationForm(AuthenticationForm):
    """Login form with Bootstrap styling."""
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter password"
        })
    )


# ==============================
# 🌍 DESTINATION FORM (Sorted Country List)
# ==============================
class DestinationForm(forms.ModelForm):
    """Form for adding or updating travel destinations."""
    location = forms.ChoiceField(
        choices=[("", "Select a country")] + sorted(countries, key=lambda c: c[1]),  # A–Z list + default placeholder
        widget=CountrySelectWidget(attrs={
            "class": "form-select"
        }),
        required=False,
        label="Country"
    )

    class Meta:
        model = Destination
        fields = ["name", "location", "status"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter destination name"
            }),
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }
        labels = {
            "name": "Destination Name",
            "status": "Status",
        }


# ==============================
# 🧑‍💻 USER UPDATE FORM
# ==============================
class UserUpdateForm(forms.ModelForm):
    """Allows users to update their username and email."""
    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Update username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Update email address"
            }),
        }
        labels = {
            "username": "Username",
            "email": "Email",
        }


# ==============================
# 🖼️ PROFILE UPDATE FORM
# ==============================
class ProfileUpdateForm(forms.ModelForm):
    """Allows users to upload or update profile picture."""
    class Meta:
        model = UserProfile
        fields = ["profile_picture"]
        widgets = {
            "profile_picture": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*"
            }),
        }
        labels = {
            "profile_picture": "Profile Picture",
        }
