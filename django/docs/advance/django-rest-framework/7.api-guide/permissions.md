# Django REST Framework: Permissions

---

## **Key Permission Classes**

---

### 1. **AllowAny**

- **Description**: Grants unrestricted access, regardless of authentication status.

```python
from rest_framework.permissions import AllowAny
class ExampleView(APIView):
    permission_classes = [AllowAny]
```

---

### 2. **IsAuthenticated**

- **Description**: Grants access only to authenticated users.

```python
from rest_framework.permissions import IsAuthenticated
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
```

---

### 3. **IsAdminUser**

- **Description**: Grants access only to users with `is_staff=True`.

```python
from rest_framework.permissions import IsAdminUser
class ExampleView(APIView):
    permission_classes = [IsAdminUser]
```

---

### 4. **IsAuthenticatedOrReadOnly**

- **Description**: Authenticated users can perform all actions, unauthenticated users are restricted to safe methods like `GET`.

```python
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class ExampleView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
```

---

## **Object-Level Permissions**

- **Description**: Used to grant access to specific objects based on user ownership or role.

```python
from rest_framework.permissions import BasePermission
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
```

---

## **Setting Default Permissions Globally**

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

---

## **Comparison Summary**

| Permission Class              | Description                   | Access Policy                          |
| ----------------------------- | ----------------------------- | -------------------------------------- |
| **AllowAny**                  | Unrestricted access           | Any user can access                    |
| **IsAuthenticated**           | Authenticated users only      | Denies access to unauthenticated users |
| **IsAdminUser**               | Admin users only              | Denies access to non-staff users       |
| **IsAuthenticatedOrReadOnly** | Authenticated for full access | Read-only for unauthenticated users    |

---

## **Custom Permissions**

- **Description**: Implement custom logic for specific access control.

```python
from rest_framework.permissions import BasePermission
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        # Custom logic
        return True
```

---

## **Conclusion**

Django REST Framework provides various permission classes to define access control, including basic permissions like `IsAuthenticated`, object-level permissions, and the ability to create custom permission logic. The appropriate permissions ensure that API endpoints are properly protected based on user roles or request types.
