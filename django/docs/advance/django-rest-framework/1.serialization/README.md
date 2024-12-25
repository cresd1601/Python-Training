# Tutorial 1: Serialization

Django REST Framework’s **Tutorial 1** teaches how to use serializers to transform data between complex Django model instances and JSON format, which is useful for APIs. Below is a more detailed breakdown:

### Snippet Model

We start by creating a simple model `Snippet` that represents code snippets, as shown below:

```python
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
```

This model has two fields:

- `title`: A string field with a maximum length of 100 characters.
- `code`: A text field to store the actual code snippet.

### Serializer for Snippet

The next step is to create a serializer class to handle the conversion between the model and JSON. This is done using Django REST Framework's `serializers.ModelSerializer` class, which provides an efficient way to serialize data:

```python
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code']
```

In this `SnippetSerializer` class:

- We specify that the serializer works with the `Snippet` model.
- The `fields` attribute tells Django REST Framework which fields from the model should be included in the serialized output.

### Serialization (Converting Model to JSON)

Once the `SnippetSerializer` is defined, you can use it to serialize data. For instance, if we have some `Snippet` objects, they can be serialized like this:

```python
snippet = Snippet.objects.all()
serializer = SnippetSerializer(snippet, many=True)
print(serializer.data)
```

Here, `serializer.data` will output the serialized data in JSON format, which could look like this:

```json
[
  { "id": 1, "title": "Example Snippet", "code": "print('Hello World!')" },
  { "id": 2, "title": "Another Snippet", "code": "def foo(): pass" }
]
```

### Deserialization (Converting JSON to Model Instance)

The process of deserialization allows us to convert incoming JSON data into model instances. For example, when we receive some JSON data, we need to first validate it, and if valid, save it to the database:

```python
data = {'title': 'New Snippet', 'code': 'print("New Code")'}
serializer = SnippetSerializer(data=data)
if serializer.is_valid():
    snippet = serializer.save()
```

Here, the `is_valid()` method checks if the data is valid based on the fields defined in the serializer. If the validation passes, we call `serializer.save()` to create a new `Snippet` object in the database.

### ModelSerializer

In the example above, `ModelSerializer` simplifies the process of creating serializers because it automatically handles many aspects, such as:

- Mapping the model fields to serializer fields.
- Creating new instances or updating existing ones via the `save()` method.

For more complex scenarios where custom validation or additional fields are needed, `ModelSerializer` can be extended with custom methods.

### Custom Validation

You can also add custom validation to the serializer. For example, if we want to ensure that the `title` field is always unique, we can define a custom validation method:

```python
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code']

    def validate_title(self, value):
        if Snippet.objects.filter(title=value).exists():
            raise serializers.ValidationError("This title already exists.")
        return value
```

This method checks if the title already exists in the database and raises an error if it does.

### Running Custom Validation

To trigger validation in Django REST Framework, use the `is_valid()` method on the serializer. This method automatically runs all field-level and object-level validation.

```python
data = {'title': 'Example', 'code': 'Example'}
serializer = SnippetSerializer(data=data)

# Trigger the validation process
if serializer.is_valid():
    # If validation passes, you can save the object
    snippet = serializer.save()
    print("Snippet created:", snippet)
else:
    # If validation fails, print the errors
    print(serializer.errors)
```

- **`is_valid()`**: This method triggers both field-level and object-level validation.
- **`serializer.errors`**: If validation fails, the errors will be stored in this attribute.

### Working with Views and APIs

Once the serializer is ready, you can use it in views to manage API responses. For example, in a Django REST Framework view, we can return serialized data as JSON:

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Snippet
from .serializers import SnippetSerializer

@api_view(['GET'])
def snippet_list(request):
    snippets = Snippet.objects.all()
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)
```

This `snippet_list` view retrieves all `Snippet` objects, serializes them, and returns the JSON response.

## Conclusion

Serialization is a powerful tool in Django REST Framework that makes it easy to convert between Django models and formats like JSON. By using `ModelSerializer`, you can simplify your code, reducing repetition. Serializers also provide built-in data validation, and custom validation can be added for specific requirements.

In short:

- **Serializer**: Converts complex data (model instances) to JSON and vice versa.
- **ModelSerializer**: Automates much of the serialization work, mapping model fields directly.
- **Deserialization**: Converts JSON data back into Django model instances.
- **Validation**: Ensures data is valid before saving it to the database.
