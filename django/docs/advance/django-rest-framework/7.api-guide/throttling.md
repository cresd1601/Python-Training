# Django REST Framework: Throttling

---

## **Key Throttle Classes**

---

### 1. **AnonRateThrottle**

- **Description**: Limits the rate of requests for unauthenticated users based on IP address.

```python
from rest_framework.throttling import AnonRateThrottle

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
    }
}
```

---

### 2. **UserRateThrottle**

- **Description**: Limits the rate of requests for authenticated users based on user ID.

```python
from rest_framework.throttling import UserRateThrottle

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
    }
}
```

---

### 3. **ScopedRateThrottle**

- **Description**: Limits requests to specific parts of the API using a `throttle_scope`.

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'uploads': '20/day',
    }
}
```

---

## **Custom Throttles**

- **Description**: Implement custom throttles by overriding `BaseThrottle`.

```python
from rest_framework.throttling import BaseThrottle

class CustomThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return True  # Custom logic
```

---

## **Setting Default Throttling Globally**

```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day',
    }
}
```

---

## **Conclusion**

Throttling in Django REST Framework controls the rate of requests using pre-defined or custom throttling classes. It can be applied globally or at the view level, providing basic protections against service overuse.
