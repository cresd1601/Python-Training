# Django Templates

Django Templates provide a powerful mechanism for dynamically generating HTML using template files combined with data from views. This system allows for flexible rendering, content reuse, and separation of business logic from presentation.

---

## 1. Template Variables Example

Template variables in Django are placeholders that get replaced with dynamic data passed from views.

### View:

```python
from django.shortcuts import render

def greeting_view(request):
    context = {'name': 'Alice', 'age': 25}
    return render(request, 'greeting.html', context)
```

### Template (`greeting.html`):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Greeting</title>
  </head>
  <body>
    <h1>Hello, {{ name }}!</h1>
    <p>You are {{ age }} years old.</p>
  </body>
</html>
```

### Output:

```html
Hello, Alice! You are 25 years old.
```

---

## 2. Loading Templates

### Step 1: Create the HTML Template

Place your HTML file inside the `templates` directory. Ensure the folder structure matches the app’s name.

For example:

```bash
project/
│
├── app_name/
│   ├── templates/
│   │   └── app_name/
│   │       └── index.html
```

Example `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Welcome to My Site</h1>
  </body>
</html>
```

---

### Step 2: Configure the `TEMPLATES` Setting

To ensure that Django knows where to look for your templates, and to make sure your custom tags and filters are recognized, you need to properly configure the `TEMPLATES` setting in your `settings.py`.

### Example of `TEMPLATES` Setting in `settings.py`

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Include your project-level templates directory
        'APP_DIRS': True,  # Automatically includes templates from installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # Optional: Add your custom template tag libraries here, if needed
            'libraries': {  # Custom template filters/tags registration
                'my_filters': 'myapp.templatetags.my_filters',  # Register 'my_filters'
            }
        },
    },
]
```

---

### Step 3: Create a View to Load the Template

In your `views.py`, define a view that loads and renders the template:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'app_name/index.html')
```

---

### Step 4: Map the View to a URL

Add a URL pattern to `urls.py` to connect the view to a URL:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

---

### Step 5: Access the Page

Navigate to `http://localhost:8000/`, and Django will render the `index.html` file.

---

## 3. Template Tags

Django’s template language includes tags that add logic and structure to templates. Common tags include:

- `{% for %}`: Loop through items in a list.
- `{% if %}`: Conditional logic.
- `{% include %}`: Include another template inside the current template.
- `{% block %}`: Define placeholders in a base template for content to be overridden by child templates.

### Example Code:

```html
{% if user.is_authenticated %}
<p>Welcome, {{ user.username }}!</p>
{% else %}
<p>Please log in.</p>
{% endif %}
```

---

## 4. Template Inheritance

Template inheritance allows for the creation of a base template with common structure (e.g., headers, footers) that can be extended by other templates. This promotes reuse and consistency across templates.

### Base Template (`base.html`):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}My Website{% endblock %}</title>
  </head>
  <body>
    <header>
      <h1>Welcome to My Website</h1>
    </header>

    <div id="content">{% block content %}{% endblock %}</div>

    <footer>
      <p>&copy; 2024 My Website</p>
    </footer>
  </body>
</html>
```

### Child Template (`home.html`):

```html
{% extends 'base.html' %} {% block title %}Home{% endblock %} {% block content
%}
<p>This is the homepage content.</p>
{% endblock %}
```

---

## 5. Template Filters

Filters modify how data is displayed without changing the underlying logic. Django provides many built-in filters, and you can create custom filters.

### Example Built-In Filters

### View:

```python
def profile_view(request):
    profile_data = {
        'username': 'john_doe',
        'bio': 'Hello, I love coding and exploring new technologies.',
        'followers': 1023,
        'account_created': '2024-01-01'
    }
    return render(request, 'profile.html', profile_data)
```

### Template (`profile.html`):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>User Profile</title>
  </head>
  <body>
    <h1>{{ username|upper }}</h1>
    <p>{{ bio|truncatechars:30 }}</p>
    <p>{{ followers }} followers</p>
    <p>Joined on {{ account_created|date:"F j, Y" }}</p>
  </body>
</html>
```

---

## 6. Custom Template Filters

You can create your own custom filters to add specific functionality to templates.

### Custom Filter in `templatetags/my_filters.py`:

```python
from django import template

register = template.Library()

@register.filter(name='reverse_text')
def reverse_text(value):
    return value[::-1]
```

### Usage in Template:

```html
{% load my_filters %}

<p>{{ 'Hello World!'|reverse_text }}</p>
```

---

## 7. Safe HTML Rendering

Django automatically escapes HTML to prevent XSS attacks. However, you can use the `safe` filter if you need to render raw HTML.

### Example:

```html
{% autoescape off %} {{ raw_html_content|safe }} {% endautoescape %}
```

---

## 8. Including Templates within Templates

You can include one template inside another using `{% include %}`.

### Example (`main.html`):

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Main Page</title>
  </head>
  <body>
    {% include 'header.html' %}

    <h1>Main Content Area</h1>

    {% include 'footer.html' %}
  </body>
</html>
```

---

### Final Summary:

Django Templates allow for dynamic HTML generation using variables, template tags (like `for`, `if`), template inheritance, and filters (built-in and custom). You can reuse components with `{% include %}` and handle HTML output securely using filters like `safe`.

This approach makes templates modular, maintainable, and secure.

---
