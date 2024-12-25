# Django REST Framework: Routers

---

## **Key Routers**

---

### 1. **SimpleRouter**

- **Description**: A basic router that automatically maps viewset actions to URLs, handling CRUD operations without additional features.

  **Example**:

  ```python
  from rest_framework.routers import SimpleRouter
  from myapp.views import MyModelViewSet

  router = SimpleRouter()
  router.register(r'my-model', MyModelViewSet)
  ```

  **Generated Routes**:

  - `/my-model/` (GET list, POST create)
  - `/my-model/{id}/` (GET retrieve, PUT update, DELETE destroy)

---

### 2. **DefaultRouter**

- **Description**: Extends `SimpleRouter` by adding extra features such as an **API root view** (at `/`) and **format suffixes** (like `.json`, `.xml`), enhancing API functionality.

  **Example**:

  ```python
  from rest_framework.routers import DefaultRouter
  from myapp.views import MyModelViewSet

  router = DefaultRouter()
  router.register(r'my-model', MyModelViewSet)
  ```

  **Generated Routes**:

  - Includes all routes from `SimpleRouter`
  - Adds an **API Root** at `/`
  - **Format suffixes** like `/my-model.json` or `/my-model.xml`

---

### 3. **Custom Routers**

- **Description**: You can extend or customize routers by subclassing `SimpleRouter` or `DefaultRouter` to meet specific routing requirements. This allows the addition of custom routes or the modification of existing ones.

  **Example**:

  ```python
  from rest_framework.routers import DefaultRouter

  class CustomRouter(DefaultRouter):
      def get_routes(self, viewset):
          routes = super().get_routes(viewset)
          # Custom logic here
          return routes

  router = CustomRouter()
  router.register(r'my-model', MyModelViewSet)
  ```

---

### 4. **Custom Actions with `@action`**

- **Description**: The `@action` decorator allows you to create custom routes for actions that are not part of standard CRUD operations. This is especially useful for actions like posting to a specific object or processing specific data.

  **Example**:

  ```python
  from rest_framework.decorators import action

  class MyModelViewSet(viewsets.ModelViewSet):
      @action(detail=True, methods=['post'])
      def custom_action(self, request, pk=None):
          obj = self.get_object()
          return Response({"message": f"Custom action on {obj.id}"})
  ```

  **Generated Route**:

  - `/my-model/{id}/custom_action/` (POST)

---

### 5. **Defining Routes without Routers**

- **Description**: You can manually define routes for ViewSets without using routers. This gives you full control over URL patterns but requires more configuration.

  **Example**:

  ```python
  from django.urls import path
  from myapp.views import MyModelViewSet

  my_model_list = MyModelViewSet.as_view({
      'get': 'list',
      'post': 'create'
  })

  my_model_detail = MyModelViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'delete': 'destroy'
  })

  urlpatterns = [
      path('my-model/', my_model_list, name='my-model-list'),
      path('my-model/<int:pk>/', my_model_detail, name='my-model-detail'),
  ]
  ```

  **Generated Routes**:

  - `/my-model/` (GET list, POST create)
  - `/my-model/<int:pk>/` (GET retrieve, PUT update, DELETE destroy)

---

## **Format Suffix Example**

Format suffixes allow you to specify the response format directly in the URL by appending a suffix (like `.json` or `.xml`), providing flexibility in how responses are rendered.

- **Example**:

  ```
  /my-model.json  →  Returns JSON response
  /my-model.xml   →  Returns XML response (if supported)
  ```

---

## **Conclusion**

Routers in Django REST Framework automate URL routing for ViewSets. While `SimpleRouter` provides basic CRUD routing, `DefaultRouter` adds valuable features such as an API root and format suffix support. You can customize routers to fit specific needs or manually define routes for greater control. The `@action` decorator also enables the creation of custom actions beyond standard CRUD operations.
