from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Models
from apps.feeds.models import Notification

# Serializers
from apps.feeds.serializers import NotificationSerializer

# Utils
from utils import extend_schema_view, extend_schema, StandardPagination


@extend_schema_view(
    list=extend_schema(
        summary="Retrieve user notifications",
        description="Retrieve all notifications for the current user with pagination.",
        responses={200: NotificationSerializer(many=True)},
    ),
)
class NotificationViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    pagination_class = StandardPagination

    def list(self, request, *args, **kwargs):
        """
        Retrieve all notifications for the authenticated user, with pagination.
        """
        queryset = Notification.objects.filter(user=request.user)

        # Paginate the queryset
        paginated_notifications = self.paginate_queryset(queryset)
        serializer = self.get_serializer(paginated_notifications, many=True)

        return self.get_paginated_response(serializer.data)
