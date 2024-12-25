# Django Admin Actions Overview

Django admin actions allow bulk operations on selected objects, such as updating statuses, exporting data, or custom actions. You can write custom actions by defining functions that take the `ModelAdmin`, `HttpRequest`, and `QuerySet` as arguments.

## 1. Writing Custom Actions

You can define actions to handle various tasks on multiple selected items.

### Example:

```python
@admin.action(description="Mark selected items as published")
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')
```

### Key Points:

- **Bulk Operations**: Perform operations on multiple selected objects at once.
- **Return Intermediate Pages**: Actions can redirect users to intermediate pages for further input.

---

## 2. Advanced Examples of Admin Actions

### Archiving Items in Bulk:

```python
@admin.action(description="Archive selected items")
def archive_items(modeladmin, request, queryset):
    queryset.update(status='archived')
```

### Exporting Data as CSV:

```python
import csv
from django.http import HttpResponse

@admin.action(description="Export selected items to CSV")
def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="items.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Status'])
    for obj in queryset:
        writer.writerow([obj.name, obj.status])
    return response
```

---

## 3. Adding Actions to `ModelAdmin`

To use your custom action, simply add it to your `ModelAdmin`.

### Example:

```python
class ArticleAdmin(admin.ModelAdmin):
    actions = [make_published, archive_items]
```

---

## 4. Handling Errors in Actions

You can handle exceptions in actions and notify users using `message_user()`:

```python
def make_published(modeladmin, request, queryset):
    try:
        queryset.update(status='published')
    except Exception as e:
        modeladmin.message_user(request, "Error occurred: " + str(e), messages.ERROR)
```

---

## 5. Making Actions Available Site-wide

Actions can be made available to all models by using `AdminSite.add_action()`.

### Example:

```python
admin.site.add_action(export_to_csv)
```

---

## 6. Disabling Actions

You can disable actions site-wide or for specific models.

### Disable Site-wide Action:

```python
admin.site.disable_action('delete_selected')
```

### Disable All Actions for a Model:

```python
class MyModelAdmin(admin.ModelAdmin):
    actions = None
```

---

### Conclusion:

Django’s admin actions offer a powerful and flexible way to manage bulk operations on multiple objects within the admin interface. By writing custom actions, you can automate tasks like updating statuses, exporting data, or archiving records, improving both efficiency and user experience. Advanced features such as handling errors and creating intermediary pages further enhance the capabilities of actions. When combined with other admin customizations, actions make the Django admin a robust tool for managing complex workflows.
