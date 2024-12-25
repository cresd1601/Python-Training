# Django REST Framework: Metadata

---

## **Setting the Metadata Scheme**

- **Description**: The metadata class can be set globally or per view. The default class is `SimpleMetadata`.

```python
REST_FRAMEWORK = {
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata'
}
```

---

## **Custom Metadata**

- **Description**: Custom metadata classes can be created by subclassing `BaseMetadata` and overriding `determine_metadata`.

```python
class MinimalMetadata(BaseMetadata):
    def determine_metadata(self, request, view):
        return {
            'name': view.get_view_name(),
            'description': view.get_view_description()
        }
```

---

## **Conclusion**

Django REST Framework allows flexible handling of metadata by customizing responses to `OPTIONS` requests, including schema information and resource capabilities.
