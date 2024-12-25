# Django REST Framework: Content Negotiation

---

## **Key Content Negotiation Methods**

---

### 1. **Determining the Accepted Renderer**

- **Description**: REST framework selects a renderer based on the client's `Accept` header and the server's configured renderers.

---

### 2. **Custom Content Negotiation**

- **Description**: Custom schemes can be implemented by subclassing `BaseContentNegotiation`.

```python
from rest_framework.negotiation import BaseContentNegotiation

class CustomNegotiation(BaseContentNegotiation):
    def select_parser(self, request, parsers):
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix):
        return (renderers[0], renderers[0].media_type)
```

---

## **Setting the Content Negotiation**

- **Description**: The default content negotiation class can be set globally in the settings.

```python
REST_FRAMEWORK = {
    'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'myapp.negotiation.CustomNegotiation',
}
```

---

## **Conclusion**

Django REST Framework provides flexible content negotiation through built-in and custom methods, allowing API responses to be tailored based on client preferences.
