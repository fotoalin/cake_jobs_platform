import json

from django.core import serializers
from django.core.management.base import BaseCommand
from faker import Faker

from courses.models import Course, CourseProgress
from jobs.models import Job
from users.models import CustomUser


class Command(BaseCommand):
    help = "Generate fixtures for CustomUser, Course, CourseProgress, and Job models using Faker"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Generate fake data for CustomUser
        users = []
        for _ in range(10):
            user = CustomUser.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                is_decorator=fake.boolean(),
                is_instructor=fake.boolean(),
                is_subscriber=fake.boolean(),
                is_admin=fake.boolean(),
                is_staff=fake.boolean(),
                is_active=fake.boolean(),
            )
            users.append(user)

        # Generate fake data for Course
        courses = []
        for _ in range(10):
            course = Course.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.text(),
                is_online=fake.boolean(),
                price=fake.pydecimal(left_digits=3, right_digits=2, positive=True),
                created_by=fake.random_element(elements=users),
            )
            # Add some subscribed users to the course
            course.subscribed_users.set(
                fake.random_elements(elements=users, length=5, unique=True)
            )
            course.image_url = fake.image_url()  # Add random image URL
            course.save()
            courses.append(course)

        # Generate fake data for CourseProgress
        course_progresses = []
        for user in users:
            for course in courses:
                progress = CourseProgress.objects.create(
                    user=user,
                    course=course,
                    progress=fake.pyfloat(
                        left_digits=1, right_digits=2, positive=True, max_value=1.0
                    ),
                )
                course_progresses.append(progress)

        # Generate fake data for Job
        jobs = []
        for _ in range(10):
            job = Job.objects.create(
                title=fake.job(),
                description=fake.text(),
                location=fake.city(),
                created_by=fake.random_element(elements=users),
            )
            # Add some subscribed users to the job
            job.subscribed_users.set(
                fake.random_elements(elements=users, length=5, unique=True)
            )
            jobs.append(job)

        # Serialize data to JSON fixtures
        user_fixture = serializers.serialize("json", users, indent=4)
        course_fixture = serializers.serialize("json", courses, indent=4)
        course_progress_fixture = serializers.serialize(
            "json", course_progresses, indent=4
        )
        job_fixture = serializers.serialize("json", jobs, indent=4)

        # Save fixtures to respective directories
        with open("users/fixtures/users.json", "w") as f:
            f.write(user_fixture)
        with open("courses/fixtures/courses.json", "w") as f:
            f.write(course_fixture)
        with open("courses/fixtures/course_progress.json", "w") as f:
            f.write(course_progress_fixture)
        with open("jobs/fixtures/jobs.json", "w") as f:
            f.write(job_fixture)

        self.stdout.write(self.style.SUCCESS("Successfully generated fixtures"))
