# courses/admin.py
from django.contrib import admin

from .models import Course, CourseProgress

# class CourseProgressInline(admin.TabularInline):
#     model = CourseProgress
#     extra = 1


# class CourseAdmin(admin.ModelAdmin):
#     list_display = ("title", "price", "is_online", "created_by")
#     search_fields = ("title",)
#     list_filter = ("is_online", "price")
#     inlines = [CourseProgressInline]


# admin.site.register(Course, CourseAdmin)


# class CourseProgressAdmin(admin.ModelAdmin):
#     list_display = ("user", "course", "progress")
#     search_fields = ("user__username", "course__title")
#     list_filter = ("progress",)


# admin.site.register(CourseProgress, CourseProgressAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
