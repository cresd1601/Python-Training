# Authentication and Permissions with `auth.User`

This tutorial demonstrates how to combine Django’s `auth.User` model with Django REST Framework’s authentication and permissions system to manage user authentication, authorization, and access control.

---

## 1. Authentication Configuration

### Global Authentication:

To apply authentication globally across the project, add the following to `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

- **BasicAuthentication**: Uses username and password for API authentication.
- **SessionAuthentication**: Uses Django’s session framework for API requests.

### View-Specific Authentication:

You can override global authentication settings for individual views:

```python
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class UserDetailView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({"message": "Authenticated user access only"})
```

This ensures that the `UserDetailView` requires users to authenticate using `BasicAuthentication` before accessing the view.

---

## 2. Permissions Configuration

Permissions determine whether an authenticated user is allowed to access a specific view or perform certain actions.

### Global Permission Configuration:

To apply global permissions for the entire project, use the following in `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

- **IsAuthenticated**: Restricts access to authenticated users only.

### View-Specific Permissions:

Permissions can also be applied per view. Here’s an example where only admin users can access the view:

```python
from rest_framework.permissions import IsAdminUser

class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        return Response({"message": "Admin access only"})
```

- **IsAdminUser**: Only allows access to admin users.

---

## 3. Permissions in Post Views

### `PostListView`: Allows reading for all users but restricts creating to authenticated users

```python
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

- **IsAuthenticatedOrReadOnly**: Allows unauthenticated users to view posts but restricts post creation to authenticated users.

### `PostDetailView`: Ensures that only the author can edit or delete a post

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .permissions import IsAuthorOrReadOnly

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
```

- **IsAuthorOrReadOnly**: Restricts modification of posts to the author, but allows read access to anyone.

---

## 4. Custom Permissions for Fine-Grained Access Control

You can create custom permissions for more granular control. For example, restricting access to a resource based on ownership:

```python
from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user  # Ensures the current user is the owner
```

### Usage in a view:

```python
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, format=None):
        profile = request.user.profile
        self.check_object_permissions(request, profile)
        return Response({"profile": profile.data})
```

- **IsOwner**: Ensures that only the owner of the object can access or modify it.

---

## 5. Combining Authentication and Permissions

You can combine authentication and permission logic to secure your API effectively. For instance:

- **All users can view posts**.
- **Only authenticated users can create posts**.
- **Only the author can modify or delete a post**.

```python
class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
```

This combination ensures that all users can read posts, but only the post author can edit or delete it.

---

## Conclusion

- **Authentication** verifies the identity of the user.
- **Permissions** determine what authenticated users can do.
- **Custom Permissions** offer fine-grained control over access.
- Combining Django's `auth.User` model with Django REST Framework's authentication and permissions system allows you to control access to your API efficiently.
