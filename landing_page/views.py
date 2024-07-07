from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse


def home_page(request):
    offers = [
        {
            "title": "Job Listings",
            "description": "Explore numerous cake decorating job opportunities from top bakeries and cake shops. Find the perfect job that suits your skills and passion.",
            "image_url": static("landing_page/images/job_listing.webp"),
            "url": reverse("jobs:jobs_list"),
            "link_text": "View Job Listings",
        },
        {
            "title": "Courses",
            "description": "Enroll in our comprehensive cake decorating courses specially designed for beginers. Learn new techniques and improve your craft with our expert instructors.",
            "image_url": static("landing_page/images/courses.webp"),
            "url": reverse("courses:courses_list"),
            "link_text": "View Courses",
        },
        {
            "title": "Support & Community",
            "description": "Join a community of cake decorators and enthusiasts. Get support, share ideas, and connect with like-minded individuals.",
            "image_url": static("landing_page/images/support.webp"),
            "url": "#",
            "link_text": "Join Community",
        },
    ]
    return render(request, "landing_page/index.html", {"offers": offers})
