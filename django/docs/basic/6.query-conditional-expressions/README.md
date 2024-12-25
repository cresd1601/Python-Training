# Django Conditional Expressions

Conditional expressions in Django allow you to use `IF...ELSE` logic in querysets. They let you define conditions and return different values based on the results of these conditions, which are particularly useful when building complex query logic.

---

## 1. Case and When

The `Case` and `When` classes are the core of conditional expressions. `Case` works like an SQL `CASE` statement and is used to specify multiple conditions, while `When` defines a condition and the result if that condition is met.

### Example Code:

```python
from django.db.models import Case, When, Value, IntegerField

# Update the discount value based on category
Product.objects.update(
    discount=Case(
        When(category='Electronics', then=Value(10)),
        When(category='Books', then=Value(5)),
        default=Value(0),
        output_field=IntegerField(),
    )
)
```

### Use Cases:

- **Multiple Conditions**: Apply different logic based on model field values.

---

## 2. Conditional Annotations

You can use conditional expressions with `annotate()` to dynamically annotate querysets based on conditional logic.

### Example Code:

```python
from django.db.models import Case, When, Value, CharField

# Annotate products with a label based on the category
Product.objects.annotate(
    category_label=Case(
        When(category='Electronics', then=Value('Electronic Device')),
        When(category='Books', then=Value('Book')),
        default=Value('Other'),
        output_field=CharField()
    )
)
```

### Use Cases:

- **Dynamic Annotations**: Add calculated fields to querysets based on conditions.

---

## 3. Combining Multiple Conditions

You can combine multiple conditions using `&` (AND) and `|` (OR) operators in `When` expressions.

### Example Code:

```python
from django.db.models import Case, When, Value

# Apply a discount if category is 'Books' and stock is greater than 100
Product.objects.update(
    discount=Case(
        When(category='Books', stock__gt=100, then=Value(15)),
        default=Value(5)
    )
)
```

### Use Cases:

- **Complex Logic**: Combine multiple conditions for more sophisticated query logic.

---

## 4. Conditional F() Expressions

You can use `F()` expressions with `Case` and `When` to compare or manipulate model fields based on conditions.

### Example Code:

```python
from django.db.models import F, Case, When, Value

# Adjust price based on quantity sold
Product.objects.update(
    final_price=Case(
        When(quantity_sold__gt=50, then=F('price') * 0.8),
        When(quantity_sold__lte=50, then=F('price') * 0.9),
        default=F('price'),
    )
)
```

### Use Cases:

- **Field Comparisons**: Update a field based on the comparison of other fields.

---

## 5. Conditional Aggregates

You can use conditional expressions with aggregation functions like `Sum`, `Count`, `Avg`, etc., to aggregate data based on conditions.

### Example Code:

```python
from django.db.models import Sum, Case, When

# Calculate total sales for products in stock
Product.objects.aggregate(
    total_sales=Sum(
        Case(
            When(stock__gt=0, then=F('price') * F('quantity_sold')),
            default=0
        )
    )
)
```

### Use Cases:

- **Conditional Aggregates**: Perform aggregate functions (e.g., sum, count) based on conditions.

---

## 6. Conditional Updates

Conditional expressions are especially useful for updating values conditionally, without having to retrieve the objects first.

### Example Code:

```python
from django.db.models import Case, When, Value

# Set a flag on products based on stock level
Product.objects.update(
    stock_flag=Case(
        When(stock__gt=50, then=Value('In Stock')),
        When(stock__lte=50, then=Value('Low Stock')),
        default=Value('Out of Stock'),
        output_field=CharField()
    )
)
```

### Use Cases:

- **Efficient Updates**: Perform conditional updates directly on the database, avoiding the need to fetch and update objects manually.

---

## 7. The `default` Argument

The `default` argument in `Case` specifies what should be returned if none of the `When` conditions are met.

### Example Code:

```python
from django.db.models import Case, When, Value

# Assign default value when no conditions match
Product.objects.annotate(
    category_label=Case(
        When(category='Electronics', then=Value('Electronic Device')),
        When(category='Books', then=Value('Book')),
        default=Value('Other')
    )
)
```

### Use Cases:

- **Fallback Values**: Ensure that a default value is returned when no conditions match.

---

### Final Comprehensive Summary:

Django Conditional Expressions allow developers to implement complex `IF...ELSE` logic in queries, making it possible to apply dynamic behavior directly within the ORM. Key features include:

1. **Case and When**: Core building blocks for conditional logic.
2. **Conditional Annotations**: Add calculated fields to querysets based on conditions.
3. **Combining Multiple Conditions**: Use logical operators to create complex conditions.
4. **F() Expressions**: Apply conditional logic to compare or update fields.
5. **Conditional Aggregates**: Perform aggregations based on conditions.
6. **Conditional Updates**: Perform conditional updates directly on the database.
7. **Default Values**: Ensure a default value is applied when no conditions are met.

By mastering these conditional expressions, you can implement more efficient, readable, and dynamic queries within Django.
