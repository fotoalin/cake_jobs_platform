# jobs/admin.py
from django.contrib import admin

from .models import Job

# def mark_as_filled(modeladmin, request, queryset):
#     queryset.update(status="filled")


# mark_as_filled.short_description = "Mark selected jobs as filled"


# class JobAdmin(admin.ModelAdmin):
#     list_display = ("title", "location", "created_by", "created_at", "status")
#     search_fields = ("title", "location")
#     list_filter = ("location", "created_at")
#     actions = [mark_as_filled]


# admin.site.register(Job, JobAdmin)


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
