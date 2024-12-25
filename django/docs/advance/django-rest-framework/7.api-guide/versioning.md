# Django REST Framework: Versioning

---

## **Key Versioning Classes**

---

### 1. **URLPathVersioning**

- **Description**: The API version is specified in the URL path.

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning'
}
```

---

### 2. **QueryParameterVersioning**

- **Description**: The version is included as a query parameter in the URL.

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    'VERSION_PARAM': 'version'
}
```

---

### 3. **AcceptHeaderVersioning**

- **Description**: The version is passed through the `Accept` header.

```python
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning'
}
```

---

## **Custom Versioning**

- **Description**: Custom versioning schemes can be created by subclassing `BaseVersioning`.

---

## **Conclusion**

Django REST Framework provides various versioning options including path, query parameter, and header-based methods, allowing developers to handle versioning based on their API needs.
