# Django REST Framework: Schemas

---

## **Generating an OpenAPI Schema**

- **Description**: Django REST Framework supports automatic schema generation for APIs using `SchemaGenerator` and `AutoSchema`.
- **Install dependencies**: `pip install pyyaml uritemplate inflection`.

---

## **Static Schema Generation**

- **Command**: Generate a static schema with the management command.

```bash
./manage.py generateschema --file openapi-schema.yml
```

---

## **Dynamic Schema Generation**

- **Helper function**: Use `get_schema_view()` to generate dynamic schemas.

```python
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("openapi", get_schema_view(title="API", version="1.0.0")),
]
```

---

## **AutoSchema**

- **Description**: Automatically generates OpenAPI-compliant schema definitions for views. It inspects the view, its serializers, fields, and response types to generate a schema.

- **Customization**: Subclass `AutoSchema` to modify the default behavior.

```python
from rest_framework.schemas import AutoSchema

class CustomAutoSchema(AutoSchema):
    def get_tags(self, path, method):
        return ['Custom Tag']

    def get_operation_id(self, path, method):
        return f"custom_{method.lower()}_{path.strip('/').replace('/', '_')}"
```

```python
class MyView(APIView):
    schema = CustomAutoSchema()
```

---

## **SchemaGenerator**

- **Description**: `SchemaGenerator` is responsible for generating the overall API schema, combining individual view schemas into a single schema document.

- **Usage**: You can use `SchemaGenerator` directly for custom schema generation or rely on helper methods like `get_schema_view()`.

```python
from rest_framework.schemas import SchemaGenerator
from rest_framework.response import Response

def generate_custom_schema(request):
    generator = SchemaGenerator(title="Custom API Schema")
    schema = generator.get_schema(request=request)
    return Response(schema)
```

- **Customization**: You can specify custom titles, descriptions, or restrict schema generation to certain URL patterns.

```python
generator = SchemaGenerator(title="My API", patterns=my_urlpatterns)
```

---

## **Custom Schema**

- **Customization**: Subclass `AutoSchema` or `SchemaGenerator` to customize schema generation according to your project’s needs.

---

## **Conclusion**

Django REST Framework allows generating both static and dynamic API schemas. With `AutoSchema`, you can generate schema definitions automatically for individual views, and with `SchemaGenerator`, you can create a complete API schema document. Customizations are possible to tailor the schema generation to specific needs.
