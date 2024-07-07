from django.urls import path

from .views import course_detail, course_list, enroll_in_course

app_name = "courses"

urlpatterns = [
    path("", course_list, name="courses_list"),
    path("<int:pk>/", course_detail, name="course_detail"),
    path("<int:pk>/enroll/", enroll_in_course, name="enroll_in_course"),
]
