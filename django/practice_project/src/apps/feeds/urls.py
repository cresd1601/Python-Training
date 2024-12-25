from django.urls import path
from apps.feeds.apis import (
    CategoryViewSet,
    PostViewSet,
    CommentViewSet,
    LikeViewSet,
    NotificationViewSet,
)

urlpatterns = [
    # Notification route
    path(
        "notifications/",
        NotificationViewSet.as_view({"get": "list"}),
        name="notification-detail",
    ),
    # Category routes
    path(
        "categories/",
        CategoryViewSet.as_view({"get": "list", "post": "create"}),
        name="category-list",
    ),
    path(
        "categories/<int:pk>/",
        CategoryViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="category-detail",
    ),
    # Post routes
    path(
        "posts/",
        PostViewSet.as_view({"get": "list", "post": "create"}),
        name="post-list",
    ),
    path(
        "posts/<int:pk>/",
        PostViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="post-detail",
    ),
    # Manually define comments routes under posts
    path(
        "posts/<int:post_id>/comments/",
        CommentViewSet.as_view(
            {"get": "list", "post": "create"},
        ),
        name="comment-list",
    ),
    path(
        "posts/<int:post_id>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"},
        ),
        name="comment-detail",
    ),
    # Manually define likes routes under posts
    path(
        "posts/<int:post_id>/like/",
        LikeViewSet.as_view({"post": "like_or_unlike"}),
        name="like-detail",
    ),
]
