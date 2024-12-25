# Django REST Framework: Exceptions

---

## **Handled Exceptions**

- **Description**: REST framework handles exceptions like `APIException`, `Http404`, and `PermissionDenied` by returning appropriate error responses.

- **Example Response**:

```json
{
  "detail": "Method 'DELETE' not allowed."
}
```

---

## **Custom Exception Handling**

- **Description**: Create a custom exception handler by extending `exception_handler`.

```python
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
    return response
```

---

## **Common Exceptions**

- `ParseError`: Malformed request data (400 Bad Request).
- `AuthenticationFailed`: Incorrect authentication (401 Unauthenticated).
- `PermissionDenied`: Insufficient permissions (403 Forbidden).

---

## **Conclusion**

Django REST Framework offers robust exception handling for API views and supports customization of error responses to fit your API design.
