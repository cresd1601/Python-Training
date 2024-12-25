from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


# Utils
from utils import (
    StandardPagination,
    extend_schema,
    extend_schema_view,
)

# Models
from apps.feeds.models import Comment

# Serializers
from apps.feeds.serializers import CommentSerializer

# Permissions
from apps.feeds.permissions import IsAuthorAdminOrReadOnlyPermission


@extend_schema_view(
    list=extend_schema(
        summary="List comments for a specific post",
        description="Retrieve a list of comments for a given post. The post ID must be provided in the URL.",
        responses={200: CommentSerializer(many=True)},
    ),
    retrieve=extend_schema(
        summary="Retrieve a single comment",
        description="Retrieve the details of a specific comment by its ID.",
        responses={200: CommentSerializer},
    ),
    create=extend_schema(
        summary="Create a new comment",
        description="Create a new comment for a specific post.",
        request=CommentSerializer,
        responses={201: CommentSerializer},
    ),
    update=extend_schema(
        summary="Update an existing comment",
        description="Update an existing comment by its ID for a specific post.",
        request=CommentSerializer,
        responses={200: CommentSerializer},
    ),
    destroy=extend_schema(
        summary="Delete a comment",
        description="Soft delete an existing comment by its ID for a specific post.",
        responses={204: None},
    ),
)
class CommentViewSet(
    CacheResponseMixin,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """
    A viewset that provides actions for listing, creating, updating,
    and deleting comments for a specific post.
    This viewset is authenticated and restricts actions based on user permissions.
    """

    permission_classes = [IsAuthenticated, IsAuthorAdminOrReadOnlyPermission]
    serializer_class = CommentSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        """
        Retrieve comments for a specific post.
        If the post does not exist, a 404 error will be raised.
        """
        post_id = self.kwargs.get("post_id")
        comment_id = self.kwargs.get("pk")

        if comment_id and post_id:
            return Comment.objects.filter(id=comment_id, post_id=post_id).active()

        return Comment.objects.filter(post_id=post_id).active()

    def perform_create(self, serializer):
        user_id = self.request.user.id
        post_id = self.kwargs.get("post_id")

        # Save the comment with the authenticated user and post ID
        serializer.save(user_id=user_id, post_id=post_id)
