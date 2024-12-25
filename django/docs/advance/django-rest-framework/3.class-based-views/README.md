# Tutorial 3: Class-Based Views

Django REST Framework’s **Tutorial 3** teaches how to rewrite API views using class-based views for better code reuse and structure. Class-based views allow you to handle different HTTP methods (GET, POST, PUT, DELETE) in a cleaner, more structured way.

## 1. Refactoring Function-Based Views to Class-Based Views

In function-based views, you handle each HTTP method explicitly like this:

```python
@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Refactoring to Class-Based Views Using `APIView`

Class-based views use Django's `APIView` to define methods like `get()`, `post()`, etc., for handling different HTTP methods:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### 2. URL Configuration for Class-Based Views

In Django, you map URLs to views using the `as_view()` method for class-based views. Here's how to connect the views to their respective URL patterns:

```python
from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),
]
```

- **`UserList.as_view()`** binds the `UserList` class to the `/users/` URL.
- **`<int:id>`** in the second URL pattern captures the user ID and passes it as a keyword argument to the `UserDetail` view.

### 3. Refactoring with Mixins

By using **mixins**, you can simplify the views by reusing common behaviors like listing and creating objects.

#### Class-Based View with Mixins:

```python
from rest_framework import mixins
from rest_framework import generics

class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

With **mixins**:

- **`ListModelMixin`** provides the functionality for listing users (used for `GET` requests).
- **`CreateModelMixin`** provides the functionality for creating users (used for `POST` requests).

### 4. Using Generic Class-Based Views for Simplicity

Django REST Framework also provides **generic views** that handle common actions like listing, creating, updating, and deleting objects.

#### Generic Class-Based View Example:

```python
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

- **`ListCreateAPIView`** automatically handles both the `GET` and `POST` requests.

For retrieving, updating, and deleting specific users, you can use:

```python
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'  # Match the 'id' in the URL pattern
```

### Conclusion

- **Class-Based Views** provide a more organized and structured way to handle multiple HTTP methods.
- **Mixins** allow you to reuse behaviors like listing, creating, updating, and deleting objects across views.
- **Generic Views** simplify common API tasks, reducing boilerplate code and making API development more efficient.
