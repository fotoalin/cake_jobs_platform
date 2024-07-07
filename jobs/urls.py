from django.urls import path

from .views import apply_for_job, job_detail, jobs_list_view

app_name = "jobs"

urlpatterns = [
    path("", jobs_list_view, name="jobs_list"),
    path("<int:job_id>/", job_detail, name="job_detail"),
    path("<int:job_id>/apply/", apply_for_job, name="apply_for_job"),
]
