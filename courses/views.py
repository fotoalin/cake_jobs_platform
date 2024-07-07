from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from users.models import CustomUser

from .models import Course

# def courses_list_view(request):
#     return render(request, "courses/index.html")


def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, "courses/course_detail.html", {"course": course})


@login_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    user = CustomUser.objects.get(
        pk=request.user.pk
    )  # Ensure we get a CustomUser instance
    if user not in course.subscribed_users.all():
        course.subscribed_users.add(user)
    return redirect(reverse("courses:course_detail", kwargs={"pk": pk}))
