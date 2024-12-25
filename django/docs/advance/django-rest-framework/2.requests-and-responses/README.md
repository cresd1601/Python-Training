# Tutorial 2: Requests and Responses

Django REST Framework’s **Tutorial 2** teaches how to handle HTTP requests and return appropriate responses using the API views. Below is a detailed explanation:

### Accessing Request Data

Django REST Framework provides an enhanced request object that allows easy access to request data like query parameters, form data, and files. For example, the request body for `POST` requests is available via `request.data`.

```python
@api_view(['POST'])
def snippet_create(request):
    print(request.data)  # Access incoming data
```

This request object extends Django’s standard `HttpRequest` and makes working with incoming JSON data, query parameters, and form submissions more consistent across HTTP methods.

### Returning a Response

The `Response` object in Django REST Framework is similar to Django’s standard `HttpResponse`, but it is more flexible and allows you to return JSON data by default.

```python
from rest_framework.response import Response

@api_view(['GET'])
def snippet_list(request):
    data = {'message': 'Hello, world!'}
    return Response(data)
```

This `Response` object automatically handles content negotiation based on the client’s request (like JSON or HTML).

### Content Negotiation

Django REST Framework uses content negotiation to determine how data should be returned to the client based on the `Accept` header. For example, if a client requests JSON data, the `Response` object automatically serializes the data into JSON.

```python
@api_view(['GET'])
def snippet_detail(request, pk):
    snippet = Snippet.objects.get(pk=pk)
    serializer = SnippetSerializer(snippet)
    return Response(serializer.data)
```

The response format (JSON, HTML, etc.) is automatically determined based on the client’s preferences.

### Using Request Methods (GET, POST, etc.)

Django REST Framework provides a decorator `@api_view` to control which HTTP methods are allowed for a view. You can handle various methods like `GET`, `POST`, `PUT`, and `DELETE`.

```python
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

In this example:

- **`status.HTTP_201_CREATED`** is used for successful POST creation.
- **`status.HTTP_400_BAD_REQUEST`** is used for invalid data.

### Handling URL Parameters with Status Codes

Django REST Framework allows you to capture URL parameters through path variables. These parameters can be passed to the view function. For example, to capture an `id` in the URL for retrieving a specific `Snippet`:

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Snippet
from .serializers import SnippetSerializer

@api_view(['GET'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
```

In this view:

- **`pk`** is a URL parameter representing the primary key of the model instance.
- **`status.HTTP_404_NOT_FOUND`** is used for handling non-existent records.

### URL Configuration

In your `urls.py`, define the URL pattern to capture the `pk` parameter from the URL:

```python
from django.urls import path
from .views import snippet_detail

urlpatterns = [
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
]
```

In this example, `<int:pk>` captures an integer from the URL and passes it as `pk` to the `snippet_detail` view.

### Query Parameters and URL Patterns

You can access query parameters using `request.query_params` in Django REST Framework. This is useful for filtering and searching.

```python
@api_view(['GET'])
def snippet_search(request):
    title = request.query_params.get('title', None)
    snippets = Snippet.objects.filter(title=title)
    serializer = SnippetSerializer(snippets, many=True)
    return Response(serializer.data)
```

In this example, the `title` query parameter is used to filter snippets with a specific title.

### Conclusion

Django REST Framework’s request and response handling makes it easier to manage HTTP interactions with APIs. Key takeaways include:

- The enhanced `Request` object simplifies access to incoming data.
- The `Response` object automatically handles content negotiation.
- View functions are decorated with `@api_view` to control allowed HTTP methods.
- Django REST Framework handles both form data and JSON seamlessly, supporting a wide range of API use cases.

In short:

- **Request**: Enhanced request object to handle incoming data.
- **Response**: Returns serialized data, automatically handling content negotiation.
- **View functions**: Decorated with `@api_view` to manage allowed HTTP methods.
- **Status Codes**: Use `rest_framework.status` for clearer and standardized HTTP status codes.
- **URL Parameters**: Capture path variables in the URL and pass them to the view for filtering or retrieving specific records.
