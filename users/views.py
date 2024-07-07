# views.py
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, redirect, render

from courses.models import Course, CourseProgress
from jobs.models import Job

from .forms import CustomUserCreationForm, LoginForm


@login_required
def dashboard(request):
    user = request.user
    enrolled_courses = Course.objects.filter(subscribed_users=user)
    course_progresses = CourseProgress.objects.filter(user=user)
    # jobs = Job.objects.filter(subscribed_users=user)
    applied_jobs = Job.objects.filter(applicants=user)

    context = {
        "user": user,
        "enrolled_courses": enrolled_courses,
        "course_progresses": course_progresses,
        "jobs": applied_jobs,
    }

    return render(
        request,
        "users/dashboard.html",
        context,
    )


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            auth_login(request, request.user)  # Log the user in after registration
            # login(request, user)  # Log the user in after registration
            return redirect("courses:courses_list")  # Redirect to a success page
    else:
        form = CustomUserCreationForm()
    return render(request, "users/registration/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("users:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "users/registration/login.html", {"form": form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("courses:courses_list")
    # return render(request, "users/registration/logout.html")
