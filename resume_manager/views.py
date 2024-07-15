from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, RESUMEUploadForm
from .models import RESUME
import pandas as pd


def home(request):
    return render(request, "home.html")


def register(request):
    user_exists = False
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                user_exists = True
            else:
                user = form.save()
                user_login(request)
                messages.success(
                    request, "Registration successful. You are now logged in."
                )
                return redirect("upload_resume")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form, "user_exists": user_exists})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful.")
            return redirect("upload_resume")  # Redirect to desired page after login
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


@login_required
def upload_resume(request):
    if request.method == "POST":
        form = RESUMEUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            if "resume_file" in request.FILES:
                csv_file = request.FILES["resume_file"]
                df = pd.read_csv(csv_file)
                resume.content = df.to_dict(orient="records")  # Store CSV data as JSON
                
                # Debugging print statements
                print("CSV File Contents:")
                print(df)
                print("Resume Content to be saved:")
                print(resume.content)
                
                resume.save()

            return redirect("view_resume")
        else:
            print("Form is not valid.")
            print(form.errors)
    else:
        form = RESUMEUploadForm()
    return render(request, "upload_resume.html", {"form": form})



@login_required
def view_resume(request):
    resume = RESUME.objects.filter(user=request.user).last()
    print(resume.content)  # Debugging line
    return render(request, "view_resume.html", {"resume": resume})



@login_required
def admin_view_users(request):
    if not request.user.is_superuser:
        return redirect("home")
    users = User.objects.all()
    return render(request, "admin_view_users.html", {"users": users})


@login_required
def view_user_resumes(request, user_id):
    if not request.user.is_superuser:
        return redirect("home")
    c_v_list = RESUME.objects.filter(user_id=user_id)
    return render(request, "view_user_resumes.html", {"resume_list": c_v_list})


@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})
