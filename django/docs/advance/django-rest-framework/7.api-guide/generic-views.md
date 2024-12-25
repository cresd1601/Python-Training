# Django REST Framework: Generic Views

The **generic views** in Django REST Framework simplify the process of writing API views by combining reusable mixins and `GenericAPIView`. Below are the key types of generic views and examples of how they are used:

### 1. **GenericAPIView**

- **Description**: A base class for all generic views. It handles commonly used methods such as retrieving querysets and serializers. It provides core functionality like pagination and filtering.
  ```python
  class MyView(GenericAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 2. **ListAPIView**

- **Description**: Provides a read-only endpoint for retrieving a list of objects. Automatically handles the `GET` request.
  ```python
  class MyListView(ListAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 3. **CreateAPIView**

- **Description**: Provides an endpoint for creating a new object. Automatically handles the `POST` request.
  ```python
  class MyCreateView(CreateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 4. **RetrieveAPIView**

- **Description**: Provides an endpoint for retrieving a single object by its primary key. Handles the `GET` request for a specific object.
  ```python
  class MyRetrieveView(RetrieveAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 5. **UpdateAPIView**

- **Description**: Provides an endpoint for updating an object. Automatically handles `PUT` and `PATCH` requests.
  ```python
  class MyUpdateView(UpdateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 6. **DestroyAPIView**

- **Description**: Provides an endpoint for deleting an object. Automatically handles `DELETE` requests.
  ```python
  class MyDeleteView(DestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 7. **ListCreateAPIView**

- **Description**: Combines both listing and creating objects in one view. It uses both `ListModelMixin` and `CreateModelMixin` under the hood to handle `GET` and `POST` requests.
  ```python
  class MyListCreateView(ListCreateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 8. **RetrieveUpdateAPIView**

- **Description**: Combines retrieving and updating objects in one view. Handles `GET`, `PUT`, and `PATCH` requests.
  ```python
  class MyRetrieveUpdateView(RetrieveUpdateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 9. **RetrieveDestroyAPIView**

- **Description**: Combines retrieving and deleting objects in one view. Handles `GET` and `DELETE` requests.
  ```python
  class MyRetrieveDestroyView(RetrieveDestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 10. **RetrieveUpdateDestroyAPIView**

- **Description**: Combines retrieving, updating, and deleting objects in one view. Handles `GET`, `PUT`, `PATCH`, and `DELETE` requests.
  ```python
  class MyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MySerializer
  ```

---

### 11. **Customizing Generic Views**

- **Description**: You can override methods like `get_queryset()` or `perform_create()` to customize the behavior of generic views.

  ```python
  class CustomListCreateView(ListCreateAPIView):
      serializer_class = MySerializer

      def get_queryset(self):
          # Return only objects related to the logged-in user
          return MyModel.objects.filter(user=self.request.user)

      def perform_create(self, serializer):
          # Automatically assign the current user to the object being created
          serializer.save(user=self.request.user)
  ```

---

## Example Usage:

```python
from rest_framework import generics
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

# Example of ListCreateAPIView
class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

# Example of RetrieveUpdateDestroyAPIView
class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```
