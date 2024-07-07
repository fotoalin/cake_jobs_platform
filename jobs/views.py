from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Job


def jobs_list_view(request):
    jobs = Job.objects.all()
    return render(request, "jobs/job_list.html", {"jobs": jobs})


def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, "jobs/job_detail.html", {"job": job})


@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    user = request.user
    if user not in job.applicants.all():
        job.applicants.add(user)
    return redirect("jobs:job_detail", job_id=job.id)
