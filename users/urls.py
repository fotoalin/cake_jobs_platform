# urls.py
from django.urls import path

from courses.views import course_list
from jobs.views import jobs_list_view

from .views import dashboard, register, user_login, user_logout

app_name = "users"

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("jobs/", jobs_list_view, name="job_list"),
    path("courses/", course_list, name="course_list"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
