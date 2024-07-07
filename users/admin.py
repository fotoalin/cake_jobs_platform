# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         ("Personal info", {"fields": ("first_name", "last_name", "email")}),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#         ("Roles", {"fields": ("is_decorator", "is_instructor")}),
#     )


# admin.site.register(CustomUser, CustomUserAdmin)


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
