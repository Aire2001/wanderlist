from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Destination
from .models import Destination, UserProfile


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )


class DestinationForm(forms.ModelForm):
    COUNTRY_CHOICES = [
        ("", "Select a country"),
        ("Afghanistan", "Afghanistan"),
        ("Albania", "Albania"),
        ("Algeria", "Algeria"),
        ("Andorra", "Andorra"),
        ("Angola", "Angola"),
        ("Argentina", "Argentina"),
        ("Armenia", "Armenia"),
        ("Australia", "Australia"),
        ("Austria", "Austria"),
        ("Azerbaijan", "Azerbaijan"),
        ("Bahamas", "Bahamas"),
        ("Bahrain", "Bahrain"),
        ("Bangladesh", "Bangladesh"),
        ("Barbados", "Barbados"),
        ("Belarus", "Belarus"),
        ("Belgium", "Belgium"),
        ("Belize", "Belize"),
        ("Benin", "Benin"),
        ("Bhutan", "Bhutan"),
        ("Bolivia", "Bolivia"),
        ("Bosnia and Herzegovina", "Bosnia and Herzegovina"),
        ("Botswana", "Botswana"),
        ("Brazil", "Brazil"),
        ("Brunei", "Brunei"),
        ("Bulgaria", "Bulgaria"),
        ("Burkina Faso", "Burkina Faso"),
        ("Burundi", "Burundi"),
        ("Cambodia", "Cambodia"),
        ("Cameroon", "Cameroon"),
        ("Canada", "Canada"),
        ("Cape Verde", "Cape Verde"),
        ("Central African Republic", "Central African Republic"),
        ("Chad", "Chad"),
        ("Chile", "Chile"),
        ("China", "China"),
        ("Colombia", "Colombia"),
        ("Comoros", "Comoros"),
        ("Costa Rica", "Costa Rica"),
        ("Croatia", "Croatia"),
        ("Cuba", "Cuba"),
        ("Cyprus", "Cyprus"),
        ("Czech Republic", "Czech Republic"),
        ("Denmark", "Denmark"),
        ("Djibouti", "Djibouti"),
        ("Dominica", "Dominica"),
        ("Dominican Republic", "Dominican Republic"),
        ("Ecuador", "Ecuador"),
        ("Egypt", "Egypt"),
        ("El Salvador", "El Salvador"),
        ("Estonia", "Estonia"),
        ("Ethiopia", "Ethiopia"),
        ("Fiji", "Fiji"),
        ("Finland", "Finland"),
        ("France", "France"),
        ("Gabon", "Gabon"),
        ("Gambia", "Gambia"),
        ("Georgia", "Georgia"),
        ("Germany", "Germany"),
        ("Ghana", "Ghana"),
        ("Greece", "Greece"),
        ("Grenada", "Grenada"),
        ("Guatemala", "Guatemala"),
        ("Guinea", "Guinea"),
        ("Guyana", "Guyana"),
        ("Haiti", "Haiti"),
        ("Honduras", "Honduras"),
        ("Hungary", "Hungary"),
        ("Iceland", "Iceland"),
        ("India", "India"),
        ("Indonesia", "Indonesia"),
        ("Iran", "Iran"),
        ("Iraq", "Iraq"),
        ("Ireland", "Ireland"),
        ("Israel", "Israel"),
        ("Italy", "Italy"),
        ("Jamaica", "Jamaica"),
        ("Japan", "Japan"),
        ("Jordan", "Jordan"),
        ("Kazakhstan", "Kazakhstan"),
        ("Kenya", "Kenya"),
        ("Kiribati", "Kiribati"),
        ("Kuwait", "Kuwait"),
        ("Kyrgyzstan", "Kyrgyzstan"),
        ("Laos", "Laos"),
        ("Latvia", "Latvia"),
        ("Lebanon", "Lebanon"),
        ("Lesotho", "Lesotho"),
        ("Liberia", "Liberia"),
        ("Libya", "Libya"),
        ("Lithuania", "Lithuania"),
        ("Luxembourg", "Luxembourg"),
        ("Madagascar", "Madagascar"),
        ("Malawi", "Malawi"),
        ("Malaysia", "Malaysia"),
        ("Maldives", "Maldives"),
        ("Mali", "Mali"),
        ("Malta", "Malta"),
        ("Mauritania", "Mauritania"),
        ("Mauritius", "Mauritius"),
        ("Mexico", "Mexico"),
        ("Moldova", "Moldova"),
        ("Monaco", "Monaco"),
        ("Mongolia", "Mongolia"),
        ("Montenegro", "Montenegro"),
        ("Morocco", "Morocco"),
        ("Mozambique", "Mozambique"),
        ("Myanmar", "Myanmar"),
        ("Namibia", "Namibia"),
        ("Nepal", "Nepal"),
        ("Netherlands", "Netherlands"),
        ("New Zealand", "New Zealand"),
        ("Nicaragua", "Nicaragua"),
        ("Niger", "Niger"),
        ("Nigeria", "Nigeria"),
        ("North Korea", "North Korea"),
        ("North Macedonia", "North Macedonia"),
        ("Norway", "Norway"),
        ("Oman", "Oman"),
        ("Pakistan", "Pakistan"),
        ("Palau", "Palau"),
        ("Panama", "Panama"),
        ("Papua New Guinea", "Papua New Guinea"),
        ("Paraguay", "Paraguay"),
        ("Peru", "Peru"),
        ("Philippines", "Philippines"),
        ("Poland", "Poland"),
        ("Portugal", "Portugal"),
        ("Qatar", "Qatar"),
        ("Romania", "Romania"),
        ("Russia", "Russia"),
        ("Rwanda", "Rwanda"),
        ("Saint Lucia", "Saint Lucia"),
        ("Saint Vincent and the Grenadines", "Saint Vincent and the Grenadines"),
        ("Samoa", "Samoa"),
        ("San Marino", "San Marino"),
        ("Saudi Arabia", "Saudi Arabia"),
        ("Senegal", "Senegal"),
        ("Serbia", "Serbia"),
        ("Seychelles", "Seychelles"),
        ("Sierra Leone", "Sierra Leone"),
        ("Singapore", "Singapore"),
        ("Slovakia", "Slovakia"),
        ("Slovenia", "Slovenia"),
        ("Solomon Islands", "Solomon Islands"),
        ("Somalia", "Somalia"),
        ("South Africa", "South Africa"),
        ("South Korea", "South Korea"),
        ("Spain", "Spain"),
        ("Sri Lanka", "Sri Lanka"),
        ("Sudan", "Sudan"),
        ("Suriname", "Suriname"),
        ("Sweden", "Sweden"),
        ("Switzerland", "Switzerland"),
        ("Syria", "Syria"),
        ("Taiwan", "Taiwan"),
        ("Tajikistan", "Tajikistan"),
        ("Tanzania", "Tanzania"),
        ("Thailand", "Thailand"),
        ("Togo", "Togo"),
        ("Tonga", "Tonga"),
        ("Trinidad and Tobago", "Trinidad and Tobago"),
        ("Tunisia", "Tunisia"),
        ("Turkey", "Turkey"),
        ("Turkmenistan", "Turkmenistan"),
        ("Uganda", "Uganda"),
        ("Ukraine", "Ukraine"),
        ("United Arab Emirates", "United Arab Emirates"),
        ("United Kingdom", "United Kingdom"),
        ("United States", "United States"),
        ("Uruguay", "Uruguay"),
        ("Uzbekistan", "Uzbekistan"),
        ("Vanuatu", "Vanuatu"),
        ("Vatican City", "Vatican City"),
        ("Venezuela", "Venezuela"),
        ("Vietnam", "Vietnam"),
        ("Yemen", "Yemen"),
        ("Zambia", "Zambia"),
        ("Zimbabwe", "Zimbabwe"),
    ]

    location = forms.ChoiceField(
        choices=COUNTRY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Destination
        fields = ['name', 'location', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

# ==============================
# ✅ PROFILE UPDATE FORM
# ==============================
class UserUpdateForm(forms.ModelForm):
    """Allows users to update their username and email"""
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Update username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Update email'
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    """Allows users to update or upload profile picture"""
    class Meta:
        model = UserProfile
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }