# Django REST Framework: Validators

---

## **Key Validators**

---

### 1. **UniqueValidator**

- **Description**: Ensures a field is unique across a model's queryset.

  **Example**:

  ```python
  from rest_framework.validators import UniqueValidator

  class MySerializer(serializers.Serializer):
      slug = serializers.SlugField(validators=[UniqueValidator(queryset=BlogPost.objects.all())])
  ```

---

### 2. **UniqueTogetherValidator**

- **Description**: Enforces a unique constraint on a combination of fields in a model.

  **Example**:

  ```python
  from rest_framework.validators import UniqueTogetherValidator

  class ExampleSerializer(serializers.Serializer):
      class Meta:
          validators = [
              UniqueTogetherValidator(queryset=ToDoItem.objects.all(), fields=['list', 'position'])
          ]
  ```

---

### 3. **UniqueForDateValidator**

- **Description**: Ensures that a field is unique within a specific date range (e.g., year, month, or day).

  **Example**:

  ```python
  from rest_framework.validators import UniqueForYearValidator

  class BlogPostSerializer(serializers.Serializer):
      class Meta:
          validators = [
              UniqueForYearValidator(queryset=BlogPost.objects.all(), field='slug', date_field='published')
          ]
  ```

---

## **Custom Validators**

---

### 1. **Function-Based Validator**

- **Description**: Custom validation using a simple function.

  **Example**:

  ```python
  def even_number(value):
      if value % 2 != 0:
          raise serializers.ValidationError('Must be an even number.')
  ```

  **Usage**:

  ```python
  class MySerializer(serializers.Serializer):
      number = serializers.IntegerField(validators=[even_number])
  ```

---

### 2. **Class-Based Validator**

- **Description**: Custom validation logic encapsulated in a class by implementing the `__call__()` method. Useful for reusability and complex validation logic.

  **Example**:

  ```python
  class MultipleOf:
      def __init__(self, base):
          self.base = base

      def __call__(self, value):
          if value % self.base != 0:
              raise serializers.ValidationError(f'Must be a multiple of {self.base}.')
  ```

  **Usage**:

  ```python
  class MySerializer(serializers.Serializer):
      number = serializers.IntegerField(validators=[MultipleOf(10)])
  ```

---

## **Advanced Field Defaults**

---

### 1. **CurrentUserDefault**

- **Description**: A default value that represents the current authenticated user.

  **Example**:

  ```python
  owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
  ```

---

### 2. **CreateOnlyDefault**

- **Description**: Provides a default value only during object creation, not during updates.

  **Example**:

  ```python
  created_at = serializers.DateTimeField(default=serializers.CreateOnlyDefault(timezone.now))
  ```

---

## **How to Use Validators in Serializers**

Validators are passed into the `validators` argument of a field in a serializer or can be applied at the `Meta` level for model serializers. Django REST Framework provides both built-in and custom validators to ensure data integrity and enforce rules during deserialization.

**Field-level validator**:

```python
class MySerializer(serializers.Serializer):
    field = serializers.CharField(validators=[UniqueValidator(queryset=MyModel.objects.all())])
```

**Object-level validator**:

```python
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']
        validators = [
            UniqueTogetherValidator(
                queryset=MyModel.objects.all(),
                fields=['field1', 'field2']
            )
        ]
```

---

## **Conclusion**

Validators in Django REST Framework enforce data integrity at both field and object levels. You can implement custom function-based or class-based validators, as well as leverage advanced defaults like `CurrentUserDefault` and `CreateOnlyDefault` for more control over data validation and creation logic. Validators are crucial for ensuring that API inputs meet specific requirements.
