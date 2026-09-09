from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register_view(request):
    if request.user.is_authenticated:
        return redirect("account")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "Please complete all fields.")
            return render(request, "users/register.html")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "users/register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "This username is already registered.")
            return render(request, "users/register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, "users/register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        login(request, user)

        messages.success(request, "Account created successfully.")

        return redirect("account")

    return render(request, "users/register.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("account")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("account")

        messages.error(request, "Invalid username or password.")

    return render(request, "users/login.html")


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("login")

    return redirect("account")


@login_required
def account_view(request):
    return render(request, "users/account.html")