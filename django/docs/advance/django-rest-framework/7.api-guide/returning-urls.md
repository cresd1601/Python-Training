# Django REST Framework: Returning URLs

---

## **reverse**

- **Description**: Similar to `django.urls.reverse`, but returns a fully qualified URL using the request to determine the host and port.

```python
from rest_framework.reverse import reverse

url = reverse('view-name', request=request)
```

- **Example Response**:

```json
{
  "url": "http://api.example.com/view-name/1/"
}
```

---

## **reverse_lazy**

- **Description**: Delays URL resolution until it's needed, returning a fully qualified URL.

```python
from rest_framework.reverse import reverse_lazy

url = reverse_lazy('view-name', request=request)
```

- **Example Response**:

```json
{
  "url": "http://api.example.com/view-name/"
}
```

---

## **Conclusion**

Using `reverse` and `reverse_lazy` ensures APIs return absolute URLs, improving clarity for API clients.
