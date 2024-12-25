from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.cache.decorators import cache_response
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
    OpenApiParameter,
    StandardPagination,
    extend_schema_view,
    extend_schema,
)

# Models
from apps.feeds.models import Post

# Serializers
from apps.feeds.serializers import PostSerializer

# Permissions
from apps.feeds.permissions import IsAuthorAdminOrReadOnlyPermission

# Documents
from apps.feeds.documents import PostDocument


@extend_schema_view(
    list=extend_schema(
        summary="List posts",
        description="Retrieve a list of active posts with optional filters.",
        responses={200: PostSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                "search",
                str,
                OpenApiParameter.QUERY,
                description="Search posts by title",
            ),
            OpenApiParameter(
                "order_by",
                str,
                OpenApiParameter.QUERY,
                description='Order posts by "comments" or "likes"',
                enum=["modified", "comments_count", "likes_count"],
            ),
            OpenApiParameter(
                "latitude",
                float,
                OpenApiParameter.QUERY,
                description="Latitude for filtering by distance",
            ),
            OpenApiParameter(
                "longitude",
                float,
                OpenApiParameter.QUERY,
                description="Longitude for filtering by distance",
            ),
            OpenApiParameter(
                "distance",
                str,
                OpenApiParameter.QUERY,
                description="The maximum distance (in kilometers) from the specified location to filter results.",
            ),
        ],
    ),
    retrieve=extend_schema(
        summary="Retrieve a single post",
        description="Retrieve details of a specific post by its ID.",
        responses={200: PostSerializer},
    ),
    create=extend_schema(
        summary="Create a new post",
        description="Create a new post with the specified content and details.",
        request=PostSerializer,
        responses={201: PostSerializer},
    ),
    update=extend_schema(
        summary="Update an existing post",
        description="Replace an existing post with new content and details. Requires the full object data.",
        request=PostSerializer,
        responses={200: PostSerializer},
    ),
    destroy=extend_schema(
        summary="Soft delete a post",
        description="Soft delete a specific post by its ID.",
    ),
)
class PostViewSet(
    CacheResponseMixin,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """
    A view for managing posts with listing, retrieving, creating, updating, and deleting functionality.
    """

    permission_classes = [IsAuthenticated, IsAuthorAdminOrReadOnlyPermission]
    serializer_class = PostSerializer
    pagination_class = StandardPagination
    document_class = PostDocument

    def get_queryset(self):
        """
        Get queryset for detail view.
        Filter by ID from URL parameters.
        """
        post_id = self.kwargs.get("pk")

        if post_id:
            return Post.objects.filter(id=post_id).active()

        return self.queryset

    @cache_response()
    def list(self, request, *args, **kwargs):
        # Get the search term from query parameters, if provided
        search = self.request.query_params.get("search")
        order_by = self.request.query_params.get("order_by")
        latitude = self.request.query_params.get("latitude")
        longitude = self.request.query_params.get("longitude")
        distance = self.request.query_params.get("distance")

        # Get all active posts by default
        posts = Post.objects.all().active().order_by("-modified")

        if search or order_by or (latitude and longitude):
            # Get all posts from Elasticsearch
            elastic_search = self.document_class.search()

            elastic_search = self.document_class.apply_search(
                elastic_search,
                search,
            )
            elastic_search = self.document_class.apply_ordering(
                elastic_search,
                order_by,
            )
            elastic_search = self.document_class.apply_distance_filtering(
                elastic_search, latitude, longitude, distance
            )

            # Get the posts from the search results
            posts = elastic_search.execute().hits

        paginated_posts = self.paginate_queryset(posts)
        serializer = self.get_serializer(paginated_posts, many=True)

        return self.get_paginated_response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
