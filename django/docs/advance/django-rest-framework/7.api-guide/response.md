# Django REST Framework: Response Properties

The `Response` class extends Django's `HttpResponse`, providing useful tools for API development. Below are the key properties and examples:

### 1. **Response Class**

- **Description**: Processes and renders data into formats like JSON, XML, etc.
  ```python
  return Response({"message": "Hello, world!"})
  ```

---

### 2. **Content Negotiation**

- **Description**: Automatically determines the response format based on the client’s `Accept` header.

---

### 3. **Status Codes**

- **Description**: Customize HTTP status codes (default is `200 OK`).
  ```python
  return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
  ```

---

### 4. **Custom Headers**

- **Description**: Add custom headers.
  ```python
  return Response({"message": "Success"}, headers={"X-Custom-Header": "MyValue"})
  ```

---

### 5. **Streaming Responses**

- **Description**: Stream large data without loading it all into memory.
  ```python
  def stream_data():
      yield "Chunk 1"
      yield "Chunk 2"
  return StreamingHttpResponse(stream_data())
  ```

---

### 6. **File Responses**

- **Description**: Serve large files like PDFs or images efficiently.
  ```python
  return FileResponse(open('file.pdf', 'rb'))
  ```

---

### 7. **Non-Data Responses**

- **Description**: Serve plain text or HTML.
  ```python
  return Response("<h1>Hello</h1>", content_type="text/html")
  ```

---

### 8. **`.template_name`**

- **Description**: Defines the template name used when rendering data with a template-based renderer.
  ```python
  return Response(data, template_name="template.html")
  ```

---

### 9. **`.exception`**

- **Description**: Used to indicate that the response was generated from an exception.
  ```python
  response.exception = True
  ```

---

### 10. **`.accepted_renderer`**

- **Description**: The renderer instance that rendered the response.
  ```python
  print(response.accepted_renderer.format)
  ```

---

### 11. **`.accepted_media_type`**

- **Description**: Media type of the response (e.g., `application/json`).
  ```python
  print(response.accepted_media_type)
  ```

---

### 12. **`.renderer_context`**

- **Description**: Dictionary containing context passed to the renderer.

---

## Example Usage:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import StreamingHttpResponse, FileResponse

class MyAPIView(APIView):

    def get(self, request):
        return Response({"message": "Hello, world!"})

    def post(self, request):
        return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED, headers={"X-Custom-Header": "AuthFailed"})

    def stream_data(self, request):
        def stream_generator():
            yield "Streaming chunk 1"
            yield "Streaming chunk 2"
        return StreamingHttpResponse(stream_generator())

    def download_file(self, request):
        return FileResponse(open('example.pdf', 'rb'))
```
