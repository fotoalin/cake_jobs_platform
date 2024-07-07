# courses/models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.templatetags.static import static

from users.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_online = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="created_courses"
    )
    subscribed_users = models.ManyToManyField(
        CustomUser, related_name="subscribed_courses"
    )
    image_url = models.URLField(default="", blank=True)
    duration = models.CharField(max_length=255)  # Add duration field
    instructor = models.CharField(max_length=255)  # Add instructor field

    def get_image_url(self):
        if self.image_url:
            return self.image_url
        # Update with the actual path to your default placeholder image
        return static("courses/images/placeholder.svg")


class CourseProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0.0)
