# Tutorial 5: Relationships and Hyperlinked APIs

Django REST Framework's **Tutorial 5** teaches how to handle relationships between models in APIs and implement hyperlinked representations for better navigation and usability in APIs.

## 1. Working with Relationships in Serializers

In this part of the tutorial, relationships between models are handled through serializers. You can represent relationships using primary keys, but a more user-friendly approach is to use **hyperlinked relationships**.

In your `Post` and `User` models, `Post` has a foreign key to `User`, representing an author. In your serializers:

### Example with Hyperlinked Serializers:

```python
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
```

- **`HyperlinkedRelatedField`**: In the `UserSerializer`, it links a user to their posts, where `view_name='post-detail'` points to the view for individual posts.

## 2. URL Configuration for Hyperlinked APIs

Since you are using class-based views and not viewsets, you’ll manually define your URL patterns. Here’s the configuration for your views:

```python
# urls.py
from django.urls import path
from .views import PostListView, PostDetailView, UserListView, UserDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),          # List and create posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Retrieve, update, delete a post
    path('users/', UserListView.as_view(), name='user-list'),          # List all users
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve user details
]
```

- **Class-based views**: You manually map URLs to your `PostListView`, `PostDetailView`, `UserListView`, and `UserDetailView` views.
- **Hyperlinked fields**: The `posts` field in the `UserSerializer` links to the `PostDetailView` via `view_name='post-detail'`.

## 3. Pagination in Hyperlinked APIs

If you have a large dataset, pagination is important to control how many items are displayed per page. In Django REST Framework, pagination can be enabled globally by setting it in `settings.py`:

```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Number of items per page
}
```

With pagination, the API response will include metadata about the total number of results, and links to the next and previous pages:

### Example Paginated Response:

```json
{
  "count": 100,
  "next": "http://localhost:8000/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "First Post",
      "content": "This is my first post",
      "author": "john_doe",
      "created_at": "2024-10-16T08:00:00Z"
    }
    // more results...
  ]
}
```

## 4. Hyperlinked API Responses

When you access your `/users/` or `/posts/` API endpoints, the responses will contain hyperlinks for the related fields.

### Example Response for `/users/`:

```json
{
  "id": 1,
  "username": "john_doe",
  "posts": ["http://localhost:8000/posts/1/", "http://localhost:8000/posts/2/"]
}
```

### Example Response for `/posts/`:

```json
{
  "id": 1,
  "title": "First Post",
  "content": "This is my first post",
  "author": "john_doe",
  "created_at": "2024-10-16T08:00:00Z"
}
```

### Conclusion

- **Class-Based Views**: You manually define URL patterns to handle multiple HTTP methods in a structured way.
- **Hyperlinked APIs**: You use `HyperlinkedRelatedField` in your serializers to generate URLs for related objects, making the API more user-friendly.
- **Pagination**: Global pagination settings allow you to manage large datasets by limiting the number of items per page in API responses.
