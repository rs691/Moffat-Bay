from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, SignInForm, ReservationForm, TestimonialForm
from .models import CustomUser, Reservation, Testimonial
from django.utils import timezone
from django.contrib.auth.decorators import login_required









# def sign_in_up(request):
#     if request.method == 'POST':
#         if 'sign_up' in request.POST:
#             sign_up_form = SignUpForm(request.POST)
#             sign_in_form = SignInForm()
#             if sign_up_form.is_valid():
#                 user = sign_up_form.save()
#                 login(request, user)
#                 messages.success(request, 'Registration successful. You are now logged in.')
#                 return redirect('index')  # Redirect to your desired page after sign-up
#         elif 'signin' in request.POST:
#             sign_in_form = SignInForm(data=request.POST)
#             sign_up_form = SignUpForm()
#             if sign_in_form.is_valid():
#                 user = sign_in_form.get_user()
#                 login(request, user)
#                 messages.success(request, 'Login successful.')
#                 return redirect('index')  # Redirect to your desired page after sign-in
#     else:
#         sign_up_form = SignUpForm()
#         sign_in_form = SignInForm()

#     return render(request, 'sign_in_up.html', {'sign_up_form': sign_up_form, 'sign_in_form': sign_in_form})


def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')




def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('index')  # Redirect to your desired page after sign-up
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('index')  # Redirect to your desired page after sign-in
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = SignInForm()
    
    return render(request, 'sign_in.html', {'form': form})




def reservation(request):
    if request.user.is_authenticated:
        # Auto-fill form with logged-in user's details
        user = request.user
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'street': user.street,
            'city': user.city,
            'state': user.state,
            'zip': user.zip_code
        }
    else:
        initial_data = {}

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if request.user.is_authenticated:
                reservation.user = request.user  # Link reservation to user
            reservation.save()
            return redirect('success')
    else:
        form = ReservationForm(initial=initial_data)  # Pre-fill form

    return render(request, 'reservation.html', {'form': form})



def about(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')  # Fetch all testimonials
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Redirect to refresh page after submission

    return render(request, 'about.html', {'testimonials': testimonials, 'form': form})

def logout(request):
    return render(request, 'logout.html')

def profile(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')

def reservation_summary(request):
    return render(request, 'reservation_summary.html')




def reservation_summary(request):
    if request.user.is_authenticated:
        user = request.user
        today = timezone.now().date()
        past_reservations = Reservation.objects.filter(user=user, reservation_date__lt=today)
        upcoming_reservations = Reservation.objects.filter(user=user, reservation_date__gte=today)
        context = {
            'past_reservations': past_reservations,
            'upcoming_reservations': upcoming_reservations,
        }
        return render(request, 'reservation_summary.html', context)
    else:
        # Redirect to login page or show an error
        return redirect('sign_in')
    


@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_summary')
    else:
        form = ReservationForm()
    return render(request, 'create_reservation.html', {'form': form})

