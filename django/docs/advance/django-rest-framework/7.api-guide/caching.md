# Django REST Framework: Caching

---

## **Using Cache with APIView and ViewSets**

- **Description**: You can apply caching to class-based views using Django’s `cache_page` decorator, alongside `vary_on_cookie` and `vary_on_headers`.

```python
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView

class PostView(APIView):
    @method_decorator(cache_page(60 * 60 * 2))  # Cache for 2 hours
    def get(self, request):
        return Response({"title": "Post title", "body": "Post content"})
```

---

## **Using Cache with @api_view Decorator**

- **Description**: The `cache_page` and `vary_on_cookie` decorators work seamlessly with function-based views using `@api_view`.

```python
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view

@cache_page(60 * 15)
@api_view(["GET"])
def get_user_list(request):
    return Response({"user_feed": request.user.get_user_feed()})
```

---

## **Important Notes**

- **Caching**: Works only with `GET` and `HEAD` methods that return a 200 response.
- **Customization**: You can vary cache behavior by headers and cookies.

---

## **Conclusion**

Caching in Django REST Framework integrates well with Django’s cache utilities, allowing you to control caching behavior using decorators on both class-based and function-based views.
