# Django REST Framework: ViewSets

**ViewSets** in Django REST Framework are a way to combine multiple views into a single class that can handle different HTTP methods, such as `GET`, `POST`, `PUT`, `PATCH`, and `DELETE`. This makes viewsets more powerful and reusable compared to traditional class-based views.

---

### 1. **ViewSet Class**

- **Description**: The base class for all viewsets. ViewSets are designed to automatically map to URLs based on the HTTP method used.

  ```python
  from rest_framework import viewsets
  from myapp.models import MyModel
  from myapp.serializers import MyModelSerializer

  class MyModelViewSet(viewsets.ViewSet):
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

- **Description**: The `ModelViewSet` class is the most commonly used viewset and provides default implementations for list, create, retrieve, update, and destroy actions for a model.

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

- **Description**: Provides default `read-only` operations such as list and retrieve, without allowing creation, update, or deletion.

  ```python
  from rest_framework import viewsets
  from myapp.models import MyModel
  from myapp.serializers import MyModelSerializer

  class MyModelReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer
  ```

---

### 4. **Customizing ViewSets**

- **Description**: You can customize viewsets by overriding the default methods such as `list()`, `create()`, or `retrieve()`. You can also use mixins to further customize your viewsets.

  ```python
  from rest_framework import viewsets
  from myapp.models import MyModel
  from myapp.serializers import MyModelSerializer
  from rest_framework.response import Response

  class CustomViewSet(viewsets.ModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer

      def create(self, request):
          # Custom logic for creating an object
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          self.perform_create(serializer)
          return Response({"message": "Object created successfully", "data": serializer.data})
  ```

---

### 5. **Action Decorators**

- **Description**: You can define custom actions using the `@action` decorator to add extra functionality to your viewsets.

  ```python
  from rest_framework.decorators import action
  from rest_framework.response import Response

  class MyModelViewSet(viewsets.ModelViewSet):
      queryset = MyModel.objects.all()
      serializer_class = MyModelSerializer

      @action(detail=False, methods=['get'])
      def custom_action(self, request):
          data = {"message": "Custom action called"}
          return Response(data)
  ```

---

### 6. **Router Integration**

- **Description**: Viewsets are usually tied to a `Router`, which automatically handles URL routing for viewsets based on the HTTP method and action.

  ```python
  from rest_framework.routers import DefaultRouter
  from myapp.views import MyModelViewSet

  router = DefaultRouter()
  router.register(r'mymodel', MyModelViewSet)

  urlpatterns = router.urls
  ```

---

### 7. **Mixing ViewSets and APIView**

- **Description**: You can mix viewsets and APIView in the same project by using them together when you need custom behavior or specific routing.

  ```python
  from rest_framework import viewsets
  from rest_framework.views import APIView
  from rest_framework.response import Response

  class MyModelViewSet(viewsets.ModelViewSet):
      # ViewSet handling MyModel actions

  class CustomAPIView(APIView):
      # APIView for custom behavior
      def get(self, request):
          return Response({"message": "Hello from APIView"})
  ```

---

## Example Usage:

```python
from rest_framework import viewsets
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

```python
from rest_framework.routers import DefaultRouter
from myapp.views import MyModelViewSet

router = DefaultRouter()
router.register(r'mymodel', MyModelViewSet)

urlpatterns = router.urls
```
