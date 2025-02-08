from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import MaxValueValidator
from .models import CustomUser, Reservation, Testimonial # Use CustomUser instead of default User





User = get_user_model()


class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required')
    street = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    zip_code = forms.CharField(max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'street', 'city', 'state', 'zip_code')

def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.street = self.cleaned_data['street']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.zip_code = self.cleaned_data['zip_code']
        if commit:
            user.save()
        return user




class ReservationForm(forms.ModelForm):
    guests = forms.IntegerField(
    widget=forms.NumberInput(attrs={'class': 'form-control'}),
    validators=[MaxValueValidator(5)]
    )
    
    class Meta:
        model = Reservation
        fields = [
            'first_name', 'last_name', 'street', 'city', 'state', 'zip',
            'guests', 'room_type', 'check_in', 'check_out'
        ]
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-select'}),
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['first_name', 'last_name', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }


