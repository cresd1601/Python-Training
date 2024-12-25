# Django REST Framework: Renderers

---

## **Key Renderers**

---

### 1. **JSONRenderer**

- **Description**: Renders responses as JSON, the default format in Django REST Framework.

  **Example**:

  ```python
  from rest_framework.renderers import JSONRenderer

  class MyView(APIView):
      renderer_classes = [JSONRenderer]

      def get(self, request):
          return Response({"message": "Hello, world!"})
  ```

---

### 2. **TemplateHTMLRenderer**

- **Description**: Renders responses using HTML templates. Typically used for HTML views in combination with Django templates.

  **Example**:

  ```python
  from rest_framework.renderers import TemplateHTMLRenderer

  class MyHTMLView(APIView):
      renderer_classes = [TemplateHTMLRenderer]
      template_name = 'my_template.html'

      def get(self, request):
          data = {'message': "Hello, HTML!"}
          return Response(data, template_name=self.template_name)
  ```

---

### 3. **StaticHTMLRenderer**

- **Description**: Renders static HTML content without requiring a template.

  **Example**:

  ```python
  from rest_framework.renderers import StaticHTMLRenderer

  class MyStaticHTMLView(APIView):
      renderer_classes = [StaticHTMLRenderer]

      def get(self, request):
          return Response('<html><body><h1>Hello, Static HTML!</h1></body></html>')
  ```

---

### 4. **BrowsableAPIRenderer**

- **Description**: Renders a browsable web interface for API interaction, useful for development and debugging.

---

## **Custom Renderers**

- **Description**: You can create a custom renderer by subclassing `BaseRenderer` and defining how the output should be rendered.

  **Example**:

  ```python
  from rest_framework.renderers import BaseRenderer

  class PlainTextRenderer(BaseRenderer):
      media_type = 'text/plain'
      format = 'txt'

      def render(self, data, accepted_media_type=None, renderer_context=None):
          return data.encode('utf-8')
  ```

---

## **Setting Renderers**

- **Global**: Renderers can be set globally through `REST_FRAMEWORK` settings in `settings.py`.

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': [
          'rest_framework.renderers.JSONRenderer',
          'rest_framework.renderers.TemplateHTMLRenderer',
      ]
  }
  ```

- **Per View**: Renderers can also be set per view by specifying `renderer_classes`.

  ```python
  class MyView(APIView):
      renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
  ```

---

## **Third-Party Renderers**

- **Description**: You can extend the supported formats by using third-party renderers such as for XML, YAML, or XLSX.

---

## **Content Negotiation**

- **Description**: Django REST Framework automatically selects the appropriate renderer by inspecting the `Accept` header of the request or using format suffixes.

  **Example**:

  ```url
  /my-api/?format=json  # Returns JSON
  /my-api/?format=html  # Returns HTML
  ```

---

## **Conclusion**

Renderers in Django REST Framework manage how responses are formatted. The default renderer is `JSONRenderer`, but you can specify others like `TemplateHTMLRenderer` for HTML output. You can also create custom renderers to support additional formats. Renderers can be applied globally or per view, and content negotiation helps determine the best format based on the request.
