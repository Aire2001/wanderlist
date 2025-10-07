from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    DestinationForm,
    UserUpdateForm,
    ProfileUpdateForm,
)
from .models import Destination, UserProfile


# ============================
# ✅ HOME PAGE
# ============================
def home(request):
    return render(request, "home.html")


# ============================
# ✅ ABOUT PAGE
# ============================
def about(request):
    return render(request, "about.html")


# ============================
# ✅ USER PROFILE VIEW / EDIT
# ============================
@login_required
@csrf_protect
def profile_view(request):
    """
    View and update the logged-in user's profile.
    Automatically creates a profile if missing.
    """
    user = request.user
    profile, _ = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "✅ Profile updated successfully!")
            return redirect("profile")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(
        request,
        "profile.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "profile": profile,
        },
    )


# ============================
# ✅ USER REGISTRATION
# ============================
@csrf_protect
def register_view(request):
    """
    Handles user registration and auto-login.
    Ensures a UserProfile is created for the new user.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.get_or_create(user=user)
            login(request, user)
            messages.success(
                request,
                f"🎉 Welcome, {user.username}! Your WanderList account was created successfully."
            )
            return redirect("destination_list")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


# ============================
# ✅ USER LOGIN
# ============================
@csrf_protect
def login_view(request):
    """
    Handles user login using a custom authentication form.
    Automatically creates a profile if missing.
    """
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            UserProfile.objects.get_or_create(user=user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            next_page = request.GET.get("next", "destination_list")
            return redirect(next_page)
        else:
            messages.error(request, "❌ Invalid username or password.")
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})


# ============================
# ✅ USER LOGOUT
# ============================
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "👋 You have been logged out successfully.")
    return redirect("login")


# ============================
# ✅ DESTINATIONS (CRUD)
# ============================

@login_required
def destination_list(request):
    """
    Display all destinations belonging to the logged-in user.
    Ordered by last update or creation.
    """
    destinations = Destination.objects.filter(user=request.user).order_by(
        "-updated_at", "-created_at"
    )
    return render(
        request,
        "destinations/destination_list.html",
        {"destinations": destinations},
    )


@login_required
@csrf_protect
def destination_create(request):
    """
    Create a new travel destination for the logged-in user.
    """
    if request.method == "POST":
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()
            messages.success(request, f"✅ '{destination.name}' added successfully!")
            return redirect("destination_list")
        else:
            messages.error(request, "⚠️ Please correct the form errors below.")
    else:
        form = DestinationForm()

    return render(request, "destinations/destination_form.html", {"form": form})


@login_required
@csrf_protect
def destination_update(request, pk):
    """
    Update an existing destination and refresh updated_at timestamp.
    """
    destination = get_object_or_404(Destination, pk=pk, user=request.user)

    if request.method == "POST":
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            updated_destination = form.save()
            messages.success(
                request,
                f"✏️ '{updated_destination.name}' updated successfully!",
            )
            return redirect("destination_list")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = DestinationForm(instance=destination)

    return render(
        request,
        "destinations/destination_form.html",
        {"form": form, "destination": destination},
    )


@login_required
@csrf_protect
def destination_delete(request, pk):
    """
    Delete a specific destination belonging to the logged-in user.
    """
    destination = get_object_or_404(Destination, pk=pk, user=request.user)
    if request.method == "POST":
        name = destination.name
        destination.delete()
        messages.success(request, f"🗑 '{name}' deleted successfully.")
        return redirect("destination_list")

    return render(
        request,
        "destinations/destination_confirm_delete.html",
        {"destination": destination},
    )
