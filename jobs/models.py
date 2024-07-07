# jobs/models.py
from django.db import models

from users.models import CustomUser


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subscribed_users = models.ManyToManyField(
        CustomUser, related_name="subscribed_jobs"
    )
    applicants = models.ManyToManyField(
        CustomUser, related_name="applied_jobs", blank=True
    )  # New field

    def __str__(self):
        return self.title
