from django.contrib import admin
from .models import Post, Category, Hashtag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)  # Allows search by category name


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "category")
    search_fields = (
        "title",
        "content",
        "user__username",
    )  # Allows search by title, content, and user username
    actions = ["activate_posts", "deactivate_posts"]

    # def activate_posts(self, request, queryset):
    #     queryset.update(status=1)  # Sets status to active
    #     self.message_user(request, "Selected posts have been activated.")

    # activate_posts.short_description = "Activate selected posts"

    # def deactivate_posts(self, request, queryset):
    #     queryset.update(status=0)  # Sets status to inactive
    #     self.message_user(request, "Selected posts have been deactivated.")

    # deactivate_posts.short_description = "Deactivate selected posts"


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)  # Allows search by hashtag name
