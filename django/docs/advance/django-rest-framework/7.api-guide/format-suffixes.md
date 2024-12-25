# Django REST Framework: Format Suffixes

---

## **format_suffix_patterns**

- **Description**: Allows appending format suffixes (like `.json`, `.html`) to URL patterns, providing different media types for the same endpoint.

```python
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('comments/', views.comment_list),
    path('comments/<int:pk>/', views.comment_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
```

---

## **Query Parameter Formats**

- **Description**: An alternative to format suffixes using the `format` query parameter (e.g., `?format=csv`).

---

## **Accept Headers vs. Format Suffixes**

- **Description**: Format suffixes are considered acceptable alongside `Accept` headers for content negotiation.

---

## **Conclusion**

Django REST Framework supports format suffixes and query parameters for content negotiation, making it flexible to work with various media types.
