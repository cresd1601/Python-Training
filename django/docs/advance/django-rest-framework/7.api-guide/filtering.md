# Django REST Framework: Filtering

---

## **Filtering Methods**

---

### 1. **Filtering against the current user**

- **Description**: Filter the queryset to show results only relevant to the authenticated user.

```python
def get_queryset(self):
    return Purchase.objects.filter(purchaser=self.request.user)
```

---

### 2. **Filtering against the URL**

- **Description**: Filter the queryset based on URL patterns.

```python
def get_queryset(self):
    username = self.kwargs['username']
    return Purchase.objects.filter(purchaser__username=username)
```

---

### 3. **Filtering against query parameters**

- **Description**: Filter the queryset based on URL query parameters.

```python
def get_queryset(self):
    username = self.request.query_params.get('username', None)
    return Purchase.objects.filter(purchaser__username=username)
```

---

## **Generic Filtering Backends**

---

### 1. **DjangoFilterBackend**

- **Description**: Allows advanced field filtering using the `django-filter` package.

```python
from django_filters.rest_framework import DjangoFilterBackend

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock']
```

---

### 2. **SearchFilter**

- **Description**: Simple single query parameter-based searching.

```python
from rest_framework import filters

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
```

---

### 3. **OrderingFilter**

- **Description**: Allows results to be ordered by a specified field using query parameters.

```python
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'name']
```

---

## **Custom Filter Backends**

---

- **Description**: Create custom filter logic by subclassing `BaseFilterBackend`.

```python
from rest_framework.filters import BaseFilterBackend

class IsOwnerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)
```

---

## **Conclusion**

Django REST Framework supports various filtering methods, including filtering by current user, URL, and query parameters. Generic backends like `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter` provide flexible solutions for filtering and searching through API data.
