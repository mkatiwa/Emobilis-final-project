from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import EmergencyAlert, ContactMessage
from django.forms.widgets import TextInput, PasswordInput
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'username',
                'email',
                'password1',
                'password2',
            ]
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    # Add geolocation fields to the form
    latitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = ContactMessage
        fields = [
            'full_name', 
            'email', 
            'phone_number', 
            'subject', 
            'message', 
            'urgency',
            'latitude',
            'longitude'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (Optional)'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Your message',
                'rows': 5
            }),
            'urgency': forms.Select(attrs={'class': 'form-control'})
        }

class EmergencyAlertForm(forms.ModelForm):
    class Meta:
        model = EmergencyAlert
        fields = [
            'full_name', 
            'phone_number', 
            'location', 
            'emergency_type', 
            'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }