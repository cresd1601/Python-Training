# Django REST Framework: Views, Generic Views, and ViewSets

---

## **Key Views**

---

### 1. **APIView**

- **Description**: The base class for all views in Django REST Framework. `APIView` provides core functionality like request parsing, response rendering, authentication, and content negotiation. It doesn't enforce specific actions (like list, create, update), giving you flexibility to define methods like `get()`, `post()`, `put()`, etc.
- **Actions**: You need to manually define actions like `get()`, `post()`, `put()`, and `delete()`.

  **Example**:

  ```python
  from rest_framework.views import APIView
  from rest_framework.response import Response

  class MyAPIView(APIView):
      def get(self, request):
          return Response({"message": "GET request successful"})

      def post(self, request):
          return Response({"message": "POST request successful"})
  ```

---

## **Key Generic Views**

---

### 1. **GenericAPIView**

- **Description**: The base class for all generic views. It provides core functionality like retrieving querysets, handling serializers, and supporting pagination and filtering.
- **Actions**: You need to manually define actions like `get()`, `post()`, `put()`, etc.

  **Example**:

  ```python
  from rest_framework.generics import GenericAPIView
  from rest_framework.response import Response

  class MyGenericAPIView(GenericAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer

      def get(self, request):
          return Response({"message": "GET request successful"})
  ```

---

### 2. **ListAPIView**

- **Description**: Provides a read-only view for listing multiple objects.
- **Actions**: Automatically handles `GET` requests for listing objects.

  **Example**:

  ```python
  from rest_framework.generics import ListAPIView

  class MyListView(ListAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 3. **RetrieveAPIView**

- **Description**: Provides a view for retrieving a single object by its primary key.
- **Actions**: Handles `GET` requests for retrieving a specific object.

  **Example**:

  ```python
  from rest_framework.generics import RetrieveAPIView

  class MyRetrieveView(RetrieveAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 4. **CreateAPIView**

- **Description**: Provides a view for creating a new object.
- **Actions**: Handles `POST` requests to create a new object.

  **Example**:

  ```python
  from rest_framework.generics import CreateAPIView

  class MyCreateView(CreateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 5. **UpdateAPIView**

- **Description**: Provides a view for updating an existing object.
- **Actions**: Handles `PUT` and `PATCH` requests for updating an object.

  **Example**:

  ```python
  from rest_framework.generics import UpdateAPIView

  class MyUpdateView(UpdateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 6. **DestroyAPIView**

- **Description**: Provides a view for deleting an object.
- **Actions**: Handles `DELETE` requests for deleting an object.

  **Example**:

  ```python
  from rest_framework.generics import DestroyAPIView

  class MyDeleteView(DestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 7. **ListCreateAPIView**

- **Description**: Combines both listing and creating objects in a single view.
- **Actions**: Handles `GET` for listing and `POST` for creating objects.

  **Example**:

  ```python
  from rest_framework.generics import ListCreateAPIView

  class MyListCreateView(ListCreateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 8. **RetrieveUpdateAPIView**

- **Description**: Combines retrieving and updating objects in a single view.
- **Actions**: Handles `GET`, `PUT`, and `PATCH` requests for retrieving and updating objects.

  **Example**:

  ```python
  from rest_framework.generics import RetrieveUpdateAPIView

  class MyRetrieveUpdateView(RetrieveUpdateAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 9. **RetrieveDestroyAPIView**

- **Description**: Combines retrieving and deleting objects in one view.
- **Actions**: Handles `GET` and `DELETE` requests for retrieving and deleting objects.

  **Example**:

  ```python
  from rest_framework.generics import RetrieveDestroyAPIView

  class MyRetrieveDestroyView(RetrieveDestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 10. **RetrieveUpdateDestroyAPIView**

- **Description**: Combines retrieving, updating, and deleting objects in a single view.
- **Actions**: Handles `GET`, `PUT`, `PATCH`, and `DELETE` requests for retrieving, updating, and deleting objects.

  **Example**:

  ```python
  from rest_framework.generics import RetrieveUpdateDestroyAPIView

  class MyRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

## **Key ViewSets**

---

### 1. **ViewSet**

- **Description**: The base class for all viewsets, providing flexible methods for handling various HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) within a single class.
- **Actions**: Typically, you need to define the actions (like `list()`, `retrieve()`, `create()`, etc.) manually.

  **Example**:

  ```python
  from rest_framework import viewsets
  from myapp.models import MyModel
  from myapp.serializers import MyModelSerializer

  class MyViewSet(viewsets.ViewSet):
      def list(self, request):
          queryset = MyModel.objects.all()
          serializer = MyModelSerializer(queryset, many=True)
          return Response(serializer.data)

      def retrieve(self, request, pk=None):
          queryset = MyModel.objects.all()
          mymodel = get_object_or_404(queryset, pk=pk)
          serializer = MyModelSerializer(mymodel)
          return Response(serializer.data)
  ```

---

### 2. **ModelViewSet**

- **Description**: Inherits from `ViewSet` and provides a full set of default actions (`list()`, `retrieve()`, `create()`, `update()`, `partial_update()`, and `destroy()`).
- **Actions**: Automatically maps to CRUD operations.

  **Example**:

  ```python
  from rest_framework import viewsets
  from myapp.models import MyModel
  from myapp.serializers import MyModelSerializer

  class MyModelViewSet(viewsets.ModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 3. **ReadOnlyModelViewSet**

- **Description**: Similar to `ModelViewSet` but provides only read-only operations (`list()` and `retrieve()`).
- **Actions**: Only supports `GET` requests (`list()` and `retrieve()`).

  **Example**:

  ```python
  from rest_framework import viewsets
  from myapp.models import MyModel
  from myapp.serializers import MyModelSerializer

  class MyReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---
