# Django REST Framework: Settings

---

## **Key Settings**

---

### 1. **DEFAULT_RENDERER_CLASSES**

- **Description**: Specifies the default classes for rendering responses.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer']
  }
  ```

---

### 2. **DEFAULT_AUTHENTICATION_CLASSES**

- **Description**: Sets the authentication backends used for API views.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication']
  }
  ```

---

### 3. **DEFAULT_PERMISSION_CLASSES**

- **Description**: Controls access to API views using permission policies.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated']
  }
  ```

---

### 4. **DEFAULT_PAGINATION_CLASS**

- **Description**: Sets the pagination style for API responses.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination'
  }
  ```

---

### 5. **DEFAULT_THROTTLE_CLASSES**

- **Description**: Sets the default rate-limiting policies for API views.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.AnonRateThrottle']
  }
  ```

---

## **Advanced Settings**

### 1. **EXCEPTION_HANDLER**

- **Description**: Defines the custom handler for exceptions.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'EXCEPTION_HANDLER': 'my_project.my_app.custom_exception_handler'
  }
  ```

---

### 2. **DEFAULT_FILTER_BACKENDS**

- **Description**: Sets default filtering backends for API views.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
  }
  ```

---

### 3. **DEFAULT_SCHEMA_CLASS**

- **Description**: Defines the schema generator class for API documentation.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.openapi.AutoSchema'
  }
  ```

---

### 4. **TEST_REQUEST_DEFAULT_FORMAT**

- **Description**: Default format for test requests.

  **Example**:

  ```python
  REST_FRAMEWORK = {
      'TEST_REQUEST_DEFAULT_FORMAT': 'json'
  }
  ```

---

## **Conclusion**

Django REST Framework's settings allow fine-tuned control over rendering, authentication, permissions, pagination, and throttling. Advanced configurations support customization for exceptions, filtering, schema generation, and testing. This flexibility ensures APIs can be tailored to specific project needs.
