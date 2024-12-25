# Django Managers

Django Managers handle database queries for your models and provide an interface to interact with the database. By using custom managers, you can simplify query logic and make your code more readable and reusable.

---

## 1. Default Manager

Django models come with a default manager called `objects`. This is automatically available on every model for querying the database.

- **`objects`**: This manager allows you to retrieve data from the database.

### Example Code:

```python
# Assuming you have a model like this
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

# You can use the default manager to get all books
all_books = Book.objects.all()  # This will return all books in the database.
```

### Use Cases:

- Retrieve all instances of the model from the database using `all()` or filtered queries like `filter()`, `get()`, etc.

---

## 2. Custom Managers

You can define custom managers to encapsulate query logic that you often reuse. Custom managers allow you to write more complex queries in a reusable way.

### Example Code:

```python
# Custom manager that returns only published books
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

# Applying the manager to a model
class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    # Use PublishedManager instead of the default objects manager
    objects = PublishedManager()

# Using the custom manager to get published books
published_books = Book.objects.all()  # This will only return books where status is 'published'
```

### Use Cases:

- **Common Query Logic**: If you need to filter for specific data, like "published" status, it's helpful to move that logic to a manager.

---

## 3. Adding Extra Methods

You can add custom methods to a manager for reusable query logic. This keeps your code DRY (Don't Repeat Yourself).

### Example Code:

```python
class PublishedManager(models.Manager):
    def published_books(self):
        return self.filter(status='published')

class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    objects = PublishedManager()

# Using the custom method
published_books = Book.objects.published_books()  # Calls the custom method to retrieve only published books
```

### Use Cases:

- **Complex Queries**: If you have a query that you use frequently, defining it in a method simplifies your code elsewhere in the application.

---

## 4. Modifying the Default Manager

You can replace the default manager (`objects`) with your own custom manager, giving you more control over how queries are handled.

### Example Code:

```python
# Custom manager that shows only active books by default
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='active')

class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    # Overriding the default manager
    objects = ActiveManager()

# Now, by default, you will only get books where status is 'active'
active_books = Book.objects.all()  # Only returns books with status='active'
```

### Use Cases:

- **Modify Default Behavior**: You can control the default query behavior globally for a model.

---

## 5. The `get_queryset()` Method

The `get_queryset()` method is the backbone of any manager. This method returns the base QuerySet that is used for all queries coming from the manager.

### Example Code:

```python
class ActiveManager(models.Manager):
    def get_queryset(self):
        # Returning only books with active status
        return super().get_queryset().filter(status='active')

class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    objects = ActiveManager()

# This will automatically apply the filter on all queries
active_books = Book.objects.all()  # Automatically filtered by status='active'
```

### Use Cases:

- **Reusable Query Logic**: Use `get_queryset()` to apply common query filters automatically, reducing repetition.

---

## 6. Multiple Managers

You can define multiple managers on a single model. This allows you to perform different types of queries depending on which manager you use.

### Example Code:

```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='draft')

class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    published = PublishedManager()  # Custom manager for published books
    draft = DraftManager()  # Custom manager for draft books

# Using multiple managers to get published or draft books
published_books = Book.published.all()  # Returns only published books
draft_books = Book.draft.all()  # Returns only draft books
```

### Use Cases:

- **Different Query Needs**: Use different managers for different query needs (e.g., published vs draft content).

---

## 7. The `Manager` versus `QuerySet`

While Managers can define general query behavior, QuerySets allow you to add chainable query logic. You can define custom QuerySets and then use them in managers.

### Example Code:

```python
class BookQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status='published')

class Book(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    # Connect QuerySet to Manager
    objects = BookQuerySet.as_manager()

# Now you can chain queries using your custom method
published_books = Book.objects.published()
```

### Use Cases:

- **Chainable Queries**: Using custom QuerySets allows you to define methods that can be chained with other Django QuerySet methods.

---

## 8. Manager Inheritance

You can inherit from Django’s base Manager class to extend or modify behavior.

### Example Code:

```python
class CustomManager(models.Manager):
    def get_queryset(self):
        # Only return active books
        return super().get_queryset().filter(is_active=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    # Inherit from custom manager
    objects = CustomManager()

# Now, all queries will only return active books
active_books = Book.objects.all()
```

### Use Cases:

- **Extend Manager Behavior**: You can extend the default behavior and add custom filters or methods.

---

## 9. Raw SQL Queries

Sometimes you might need to perform raw SQL queries for complex operations. Django’s managers allow you to do this with the `raw()` method.

### Example Code:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

# Use raw SQL query
books = Book.objects.raw('SELECT * FROM myapp_book WHERE author = %s', ['John Doe'])

# Iterate through the raw SQL result
for book in books:
    print(book.title)
```

### Use Cases:

- **Complex SQL**: Perform queries that are too complex for Django’s ORM, such as optimized SQL statements.

---

## 10. The `use_in_migrations` Option

When using custom managers, you may want to specify if they should be serialized in migrations. Setting `use_in_migrations` to `True` ensures the manager will be available during migrations.

### Example Code:

```python
class MyManager(models.Manager):
    use_in_migrations = True

class Book(models.Model):
    title = models.CharField(max_length=100)
    objects = MyManager()
```

### Use Cases:

- **Migrations**: Control whether the manager should be serialized into the migration files.

---

### Final Comprehensive Summary:

By customizing Django managers, you can improve query logic, keep code DRY, and perform more complex queries in a reusable and maintainable way.
