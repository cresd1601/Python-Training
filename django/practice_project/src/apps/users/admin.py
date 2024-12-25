from django.contrib import admin

# Register your models here.
from apps.users.models import User, UserProfile


# Custom UserAdmin class
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("username", "email")
    list_filter = ("is_active", "is_staff")
    ordering = ("-date_joined",)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")
    search_fields = ("user__username", "bio")
    ordering = ("-created",)
