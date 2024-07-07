# cakes_platform/admin.py
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path


class CustomAdminSite(admin.AdminSite):
    site_header = "Cake Decorating Admin"
    site_title = "Admin"
    index_title = "Dashboard"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path("stats/", self.admin_view(self.stats_view))]
        return custom_urls + urls

    def stats_view(self, request):
        context = dict(
            self.each_context(request),
            key="value",
        )
        return TemplateResponse(request, "admin/stats.html", context)


admin_site = CustomAdminSite(name="custom_admin")

from courses.models import Course, CourseProgress
from jobs.models import Job

# Register the custom admin site
from users.models import CustomUser

admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(Job, JobAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(CourseProgress, CourseProgressAdmin)
admin_site.register(Course, CourseAdmin)
admin_site.register(CourseProgress, CourseProgressAdmin)
