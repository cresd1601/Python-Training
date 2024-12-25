# Django REST Framework: Pagination

---

## **Key Pagination Classes**

---

### 1. **PageNumberPagination**

- **Description**: Paginates results using page numbers.

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```

---

### 2. **LimitOffsetPagination**

- **Description**: Uses limit and offset query parameters for pagination.

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
```

---

### 3. **CursorPagination**

- **Description**: Uses cursor-based pagination for large datasets.

```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'PAGE_SIZE': 100
}
```

---

## **Custom Pagination**

- **Description**: You can create custom pagination styles by subclassing `BasePagination`.

---

## **Conclusion**

Django REST Framework supports several pagination styles, including page number, limit-offset, and cursor-based pagination. Custom pagination classes can also be created to meet specific project needs.
