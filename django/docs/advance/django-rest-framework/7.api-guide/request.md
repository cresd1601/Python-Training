# Django REST Framework: Request Properties

The `Request` class in Django REST Framework extends the standard `HttpRequest`, offering several enhanced properties for API requests:

### 1. `.data`

- **Description**: Contains the parsed content of the request body, depending on the content type (e.g., JSON or form data).
- **Example**:
  ```python
  # JSON request body: {"name": "John"}
  name = request.data.get('name')
  print(name)  # Output: "John"
  ```
- **Details**: Handles various content types like `application/json` and `multipart/form-data`. For GET requests, it is usually empty.

### 2. `.query_params`

- **Description**: Similar to Django’s `request.GET`, this contains query string parameters from the URL.
- **Example**:
  ```python
  # URL: /api/users/?search=john&page=2
  search = request.query_params.get('search')
  page = request.query_params.get('page')
  print(search, page)  # Output: "john", "2"
  ```
- **Details**: Used for filtering and pagination in query strings.

### 3. `.user`

- **Description**: Provides information about the authenticated user making the request.
- **Example**:
  ```python
  if request.user.is_authenticated:
      print(f"User: {request.user.username}")
  ```
- **Details**: Contains user information when authenticated, or an `AnonymousUser` if not.

### 4. `.auth`

- **Description**: Stores authentication information, such as tokens or credentials.
- **Example**:
  ```python
  token = request.auth
  ```

### 5. `.method`

- **Description**: The HTTP method used in the request, such as `GET`, `POST`, `PUT`, or `DELETE`.
- **Example**:
  ```python
  if request.method == 'POST':
      print("This is a POST request")
  ```

### 6. `.content_type`

- **Description**: The content type of the request body, such as `application/json`, `multipart/form-data`, etc.
- **Example**:
  ```python
  if request.content_type == 'application/json':
      print("This is a JSON request")
  ```

### 7. `.stream`

- **Description**: Provides raw access to the request body, useful for large file uploads.
- **Example**:
  ```python
  file_content = request.stream.read()
  ```

### 8. `.FILES`

- **Description**: A dictionary of files uploaded via the request.
- **Example**:
  ```python
  uploaded_file = request.FILES['file']
  print(uploaded_file.name)
  ```

### 9. `.META`

- **Description**: Contains all HTTP headers and environmental variables associated with the request.
- **Example**:
  ```python
  user_agent = request.META.get('HTTP_USER_AGENT')
  ```

### 10. `.COOKIES`

- **Description**: A dictionary of cookies sent by the client in the request.
- **Example**:
  ```python
  session_id = request.COOKIES.get('sessionid')
  ```

## Example Usage:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Query parameters
        search = request.query_params.get('search')

        # User information
        user = request.user
        print(f"Authenticated user: {user.username}")

        # Content type check
        if request.content_type == 'application/json':
            print("Request contains JSON data")

        # Access uploaded files
        uploaded_file = request.FILES.get('profile_picture')
        if uploaded_file:
            print(f"Uploaded file: {uploaded_file.name}")

        # Check request method
        if request.method == 'GET':
            print("GET request")

        return Response({
            'message': f"Hello, {user.username}",
            'search_query': search,
        })
```
