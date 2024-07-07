# urls.py
from django.urls import path

from .views import home_page

app_name = "landing_page"

urlpatterns = [
    path("", home_page, name="home_page"),
]
