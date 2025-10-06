from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm, DestinationForm
from .models import Destination


# ---------- HOME ----------
def home(request):
    return render(request, "home.html")


# ---------- ABOUT ----------
def about(request):
    return render(request, "about.html")


# ---------- PROFILE ----------
@login_required
def profile_view(request):
    return render(request, "profile.html")


# ---------- AUTH ----------
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully 🎉")
            return redirect("destination_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back 👋 {user.username}")
            return redirect("destination_list")
        else:
            messages.error(request, "Invalid username or password ❌")
    else:
        form = CustomAuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out 👋")
    return redirect("login")


# ---------- DESTINATIONS (CRUD) ----------
@login_required
def destination_list(request):
    destinations = Destination.objects.filter(user=request.user).order_by("location")
    return render(request, "destinations/destination_list.html", {"destinations": destinations})


@login_required
def destination_create(request):
    if request.method == "POST":
        form = DestinationForm(request.POST)
        if form.is_valid():
            destination = form.save(commit=False)
            destination.user = request.user  # link to logged-in user
            destination.save()
            messages.success(request, "Destination added successfully 🎉")
            return redirect("destination_list")
    else:
        form = DestinationForm()
    return render(request, "destinations/destination_form.html", {"form": form})


@login_required
def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk, user=request.user)
    if request.method == "POST":
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination updated successfully ✏️")
            return redirect("destination_list")
    else:
        form = DestinationForm(instance=destination)
    return render(request, "destinations/destination_form.html", {"form": form, "destination": destination})


@login_required
def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk, user=request.user)
    if request.method == "POST":
        destination.delete()
        messages.success(request, "Destination deleted successfully ✅")
        return redirect("destination_list")
    return render(request, "destinations/destination_confirm_delete.html", {"destination": destination})
