# Django Rest Framework: Class-Based Views Guide

Django Rest Framework (DRF) provides several tools to help developers build APIs efficiently using **class-based views**. These allow for reusable code and help to maintain the DRY principle (Don’t Repeat Yourself). Below is a summary of how to implement class-based views in DRF:

## 1. APIView Class

- `APIView` is the foundational class for DRF views. It handles content negotiation, authentication, and permission checks.
- It provides methods such as `.get()`, `.post()`, and others to handle HTTP requests.

### Example:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelList(APIView):
    def get(self, request):
        objects = MyModel.objects.all()
        serializer = MyModelSerializer(objects, many=True)
        return Response(serializer.data)
```

## 2. Generic Views

- `GenericAPIView` extends `APIView` and simplifies common tasks like pagination, filtering, and object lookups.
- You can combine `GenericAPIView` with mixins like `ListModelMixin`, `CreateModelMixin`, etc., for CRUD actions.

### Example:

```python
from rest_framework import generics
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

## 3. Mixin Classes

- DRF mixins like `ListModelMixin`, `CreateModelMixin`, and `RetrieveModelMixin` are reusable classes for composing common behaviors.
- They help simplify actions such as creating, retrieving, updating, and deleting resources.

### Example Using Mixins:

```python
from rest_framework import generics, mixins

class MyModelDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

## 4. Pre-Built Generic Views

- DRF provides pre-built views like `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView` that automatically handle common actions.
- These help to reduce boilerplate code.

### Example Using Pre-Built Views:

```python
class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```
