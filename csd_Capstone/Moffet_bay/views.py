from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, SignInForm, ReservationForm, TestimonialForm, ReservationLookupForm, ContactMessageForm
from .models import CustomUser, Reservation, Testimonial
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date
from django.db.models import Q
from django.http import JsonResponse
import json

from django.http import HttpResponse





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

def docs_view(request):
    return render(request, 'docs.html')



@login_required
def reservation_history(request):
    today = date.today()
    return render(request, 'reservations/history.html', {'today': today})

@login_required
def past_reservations(request):
    today = date.today()
    reservations = Reservation.objects.filter(
        user=request.user,
        check_out__lt=today
    ).order_by('-check_out')
    
    return render(request, 'reservations/past_reservations.html', {
        'reservations': reservations
    })

@login_required
def future_reservations(request):
    today = date.today()
    reservations = Reservation.objects.filter(
        user=request.user,
        check_in__gte=today
    ).order_by('check_in')
    
    return render(request, 'reservations/future_reservations.html', {
        'reservations': reservations
    })
    



def register(request):
    return render(request, 'register.html')

def check_user(request):
    return render(request, 'check_user.html')

def room_rates(request):
    return render(request, 'room_rates.html')




def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            #  success message using Django's messages framework.
            messages.success(request, 'Message sent successfully.')
            return redirect('contact')  # Redirect back to the contact page or to a thank-you page.
    else:
        form = ContactMessageForm()
    
    return render(request, 'contact.html', {'form': form})


# def reservation_lookup(request):
#     form = ReservationLookupForm(request.POST or None)
#     results = None
#     if request.method == 'POST' and form.is_valid():
#         reservation_id = form.cleaned_data.get('reservation_id')
#         last_name = form.cleaned_data.get('last_name')
#         email = form.cleaned_data.get('email')
        
#         query = Q()
#         if reservation_id:
#             query &= Q(reservation_id__icontains=reservation_id)
#         if last_name:
#             query &= Q(last_name__icontains=last_name)
#         if email:
#             query &= Q(email__icontains=email)
            
#         results = Reservation.objects.filter(query)
    
#     # Check for the HTMX header
#     is_htmx = request.headers.get('HX-Request', False) or request.META.get('HTTP_HX_REQUEST', False)
    
#     if is_htmx:
#         return render(request, 'reservation_lookup_results.html', {'results': results})
    
#     return render(request, 'reservation_lookup.html', {'form': form, 'results': results})




def reservation_lookup(request):
    print("View called")
    print("Headers:", request.headers)  # Debug headers
    print("Is HTMX:", request.htmx)    # Debug HTMX status
    
    form = ReservationLookupForm(request.POST or None)
    results = None
    
    if request.method == 'POST' and form.is_valid():
        print("Form data:", form.cleaned_data)  # Debug form data
        
        reservation_id = form.cleaned_data.get('reservation_id')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        
        query = Q()
        if reservation_id:
            query &= Q(reservation_id__icontains=reservation_id)
        if last_name:
            query &= Q(last_name__icontains=last_name)
        if email:
            query &= Q(email__icontains=email)
        
        if not any([reservation_id, last_name, email]):
            results = Reservation.objects.none()
        else:
            results = Reservation.objects.filter(query)
            print("Query:", str(results.query))  # Debug query
            print("Results count:", results.count())  # Debug results
    
    context = {'form': form, 'results': results}
    
    if request.htmx:
        return render(request, 'reservation_lookup_results.html', context)
    return render(request, 'reservation_lookup.html', context)

def reservation_lookup_results(request):
    return render(request, 'reservation_lookup_results.html')