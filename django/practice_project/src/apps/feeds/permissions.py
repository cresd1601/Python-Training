from rest_framework.permissions import BasePermission


class IsAdminOrReadOnlyPermission(BasePermission):
    """
    Custom permission to allow read-only access for all users,
    and write permissions only for admin users.
    """

    def has_permission(self, request, view):
        # Allow read-only access for all users (GET method)
        if request.method in ["GET"]:
            return True
        # Allow write permissions only to admin users (staff)
        return request.user and request.user.is_staff


class IsAuthorAdminOrReadOnlyPermission(BasePermission):
    """
    Custom permission to allow:
    - The user of a comment to update or delete their comment.
    - Admin users (staff) to update or delete any comment.
    - All users can read comments (GET method).
    """

    def has_object_permission(self, request, view, obj):
        # Admin users (staff) have full permissions for PUT, DELETE, etc.
        if request.user.is_staff:
            return True

        # Authors can update or delete their own comments
        if request.method in ["PUT", "DELETE"]:
            return obj.user == request.user

        # All users can read comments (GET method)
        return request.method == "GET"
