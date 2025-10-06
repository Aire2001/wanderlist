from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    DestinationForm,
    UserUpdateForm,
    ProfileUpdateForm,
)
from .models import Destination, UserProfile


# ---------- HOME ----------
def home(request):
    return render(request, "home.html")


# ---------- ABOUT ----------
def about(request):
    return render(request, "about.html")


# ---------- PROFILE ----------
@login_required
def profile_view(request):
    """View and edit user profile (username, email, and profile picture)."""
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "✅ Profile updated successfully!")
            return redirect("profile")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": profile,
    }
    return render(request, "profile.html", context)


# ---------- AUTH ----------
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ✅ create a blank profile automatically
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, "🎉 Account created successfully!")
            return redirect("destination_list")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 Welcome back, {user.username}!")
            return redirect("destination_list")
        else:
            messages.error(request, "❌ Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "👋 You have been logged out.")
    return redirect("login")


# ---------- DESTINATIONS (CRUD) ----------
@login_required
def destination_list(request):
    destinations = Destination.objects.filter(user=request.user).order_by("-updated_at", "-created_at")
    return render(request, "destinations/destination_list.html", {"destinations": destinations})


@login_required
def destination_create(request):
    """Create a new destination."""
    if request.method == "POST":
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user
            destination.save()
            messages.success(request, f"✅ '{destination.name}' added successfully!")
            return redirect("destination_list")
        else:
            messages.error(request, "❌ Please correct the form errors.")
    else:
        form = DestinationForm()
    return render(request, "destinations/destination_form.html", {"form": form})


@login_required
def destination_update(request, pk):
    """Update an existing destination and refresh updated_at automatically."""
    destination = get_object_or_404(Destination, pk=pk, user=request.user)
    if request.method == "POST":
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            updated_destination = form.save(commit=False)
            updated_destination.save()  # auto-updates updated_at
            messages.success(
                request,
                f"✏️ '{updated_destination.name}' updated successfully on "
                f"{updated_destination.updated_at.strftime('%b %d, %Y %I:%M %p')}"
            )
            return redirect("destination_list")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = DestinationForm(instance=destination)
    return render(request, "destinations/destination_form.html", {"form": form, "destination": destination})


@login_required
def destination_delete(request, pk):
    """Delete a destination."""
    destination = get_object_or_404(Destination, pk=pk, user=request.user)
    if request.method == "POST":
        name = destination.name
        destination.delete()
        messages.success(request, f"🗑 '{name}' deleted successfully.")
        return redirect("destination_list")
    return render(request, "destinations/destination_confirm_delete.html", {"destination": destination})
