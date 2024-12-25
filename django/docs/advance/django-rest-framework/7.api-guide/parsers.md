# Django REST Framework: Parsers

---

## **Key Parsers**

---

### 1. **JSONParser**

- **Description**: Parses incoming request data as JSON.

  **Example**:

  ```python
  from rest_framework.parsers import JSONParser

  class MyView(APIView):
      parser_classes = [JSONParser]

      def post(self, request):
          data = request.data
          return Response({'received_data': data})
  ```

---

### 2. **FormParser**

- **Description**: Parses incoming request data as form data, typically used with HTML forms (`application/x-www-form-urlencoded`).

  **Example**:

  ```python
  from rest_framework.parsers import FormParser

  class MyView(APIView):
      parser_classes = [FormParser]

      def post(self, request):
          data = request.data
          return Response({'received_data': data})
  ```

---

### 3. **MultiPartParser**

- **Description**: Handles file uploads and form data, used for requests with `multipart/form-data` content type.

  **Example**:

  ```python
  from rest_framework.parsers import MultiPartParser

  class FileUploadView(APIView):
      parser_classes = [MultiPartParser]

      def post(self, request):
          file = request.data['file']
          return Response({'file_name': file.name})
  ```

---

### 4. **FileUploadParser**

- **Description**: Specializes in handling raw file uploads. Unlike `MultiPartParser`, it handles file data as binary streams without extra form fields.

  **Example**:

  ```python
  from rest_framework.parsers import FileUploadParser

  class MyFileUploadView(APIView):
      parser_classes = [FileUploadParser]

      def post(self, request):
          file = request.data['file']
          return Response({'file_name': file.name})
  ```

---

## **Custom Parsers**

- **Description**: You can create a custom parser by subclassing `BaseParser` and defining the `parse()` method to handle your desired content type.

  **Example**:

  ```python
  from rest_framework.parsers import BaseParser

  class PlainTextParser(BaseParser):
      media_type = 'text/plain'

      def parse(self, stream, media_type=None, parser_context=None):
          return stream.read().decode('utf-8')
  ```

  **Usage**:

  ```python
  class MyView(APIView):
      parser_classes = [PlainTextParser]

      def post(self, request):
          data = request.data
          return Response({'received_data': data})
  ```

---

## **Setting Parsers**

- **Global**: Parsers can be set globally via `REST_FRAMEWORK` settings in `settings.py`.

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PARSER_CLASSES': [
          'rest_framework.parsers.JSONParser',
          'rest_framework.parsers.FormParser',
      ]
  }
  ```

- **Per View**: You can set parsers for specific views by using the `parser_classes` attribute.

  ```python
  from rest_framework.parsers import MultiPartParser

  class MyView(APIView):
      parser_classes = [MultiPartParser]
  ```

---

## **Third-Party Parsers**

- **Description**: Django REST Framework supports third-party packages for parsing additional content types, such as YAML, XML, and MessagePack.

---

## **Conclusion**

Parsers in Django REST Framework determine how incoming request data is parsed into a format that views can handle. They support various content types like JSON, form data, and file uploads. You can apply parsers globally or per view, and even define custom parsers for handling specific formats. Third-party parsers are available for additional content types.
