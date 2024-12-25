from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.decorators import action

# Models
from apps.feeds.models import Post, Like

# Utils
from utils import extend_schema, extend_schema_view


@extend_schema_view(
    like_or_unlike=extend_schema(
        summary="Like or unlike a post",
        description="Allows an authenticated user to like or unlike a post. "
        "If the user has already liked the post, it will be unliked. "
        "If the user has not liked the post, it will be liked.",
        request=None,
        responses={
            HTTP_200_OK: {"message": "Post unliked"},
            HTTP_201_CREATED: {"message": "Post liked"},
        },
    )
)
class LikeViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated]

    # Custom action to like or unlike a post
    @action(detail=True, methods=["post"], url_path="like")
    def like_or_unlike(self, request, *args, **kwargs):
        post_id = self.kwargs.get("post_id")
        post = Post.objects.get(pk=post_id)

        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if created:
            return Response({"message": "Post liked"}, status=HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message": "Post unliked"}, status=HTTP_200_OK)
