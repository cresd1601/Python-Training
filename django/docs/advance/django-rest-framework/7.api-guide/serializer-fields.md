# Django REST Framework: Serializer Fields

---

## **Key Fields**

---

### 1. **BooleanField**

- **Description**: Used to represent `True`/`False` values. Maps to Python booleans.

  **Example**:

  ```python
  from rest_framework import serializers

  class MySerializer(serializers.Serializer):
      is_active = serializers.BooleanField()
  ```

---

### 2. **CharField**

- **Description**: Represents textual data. Commonly used for string inputs. Supports `max_length`, `min_length`, and `trim_whitespace`.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      name = serializers.CharField(max_length=100)
  ```

---

### 3. **ChoiceField**

- **Description**: Restricts input to a specified set of choices. Accepts a list or tuple of valid choices.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      status = serializers.ChoiceField(choices=[('draft', 'Draft'), ('published', 'Published')])
  ```

---

### 4. **DateTimeField**

- **Description**: Handles date and time inputs. Can be used for ISO 8601 strings and Python `datetime` objects.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      created = serializers.DateTimeField()
  ```

---

### 5. **DecimalField**

- **Description**: Used for decimal numbers with customizable precision and number of decimal places.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      price = serializers.DecimalField(max_digits=10, decimal_places=2)
  ```

---

### 6. **EmailField**

- **Description**: Validates an email format using Django’s built-in email validators.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      email = serializers.EmailField()
  ```

---

### 7. **FileField**

- **Description**: Handles file uploads. Requires specifying `max_length` and supports `allow_empty_file`.

  **Example**:

  ```python
  class FileUploadSerializer(serializers.Serializer):
      file = serializers.FileField()
  ```

---

### 8. **ImageField**

- **Description**: Subclass of `FileField` that specifically validates image file types.

  **Example**:

  ```python
  class ImageUploadSerializer(serializers.Serializer):
      image = serializers.ImageField()
  ```

---

### 9. **IntegerField**

- **Description**: Handles integer input. Supports options like `min_value` and `max_value`.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      age = serializers.IntegerField(min_value=0)
  ```

---

### 10. **FloatField**

- **Description**: Used for floating-point numbers. Similar to `DecimalField` but without decimal precision control.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      rating = serializers.FloatField()
  ```

---

## **Relational Fields**

---

### 1. **PrimaryKeyRelatedField**

- **Description**: Used for foreign key relationships, storing primary key values of related models.

  **Example**:

  ```python
  class MySerializer(serializers.ModelSerializer):
      related_model = serializers.PrimaryKeyRelatedField(queryset=RelatedModel.objects.all())
  ```

---

### 2. **SlugRelatedField**

- **Description**: Similar to `PrimaryKeyRelatedField`, but references related objects by a unique slug field.

  **Example**:

  ```python
  class MySerializer(serializers.ModelSerializer):
      category = serializers.SlugRelatedField(slug_field='slug', queryset=Category.objects.all())
  ```

---

### 3. **HyperlinkedRelatedField**

- **Description**: Represents relationships using URLs instead of primary keys.

  **Example**:

  ```python
  class MySerializer(serializers.ModelSerializer):
      user = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())
  ```

---

## **Custom Fields**

- **Description**: Custom fields can be created by subclassing `Field` and overriding `to_representation()` and `to_internal_value()`.

  **Example**:

  ```python
  class UpperCaseField(serializers.Field):
      def to_representation(self, value):
          return value.upper()

      def to_internal_value(self, data):
          return data.lower()
  ```

---

## **Field Arguments**

- **Core arguments**:

  - **`read_only`**: Marks the field as read-only, skipping validation on write operations.
  - **`write_only`**: Only available during input and not during serialization.
  - **`required`**: Ensures the field is mandatory during input.
  - **`default`**: Sets a default value if none is provided.
  - **`allow_null`**: Allows `null` values to be accepted.
  - **`validators`**: Accepts a list of validators for custom validation logic.

  **Example**:

  ```python
  class MySerializer(serializers.Serializer):
      username = serializers.CharField(required=True, default="guest")
      email = serializers.EmailField(validators=[validate_email])
  ```

---

## **Conclusion**

Django REST Framework's fields enable the mapping of complex data into native Python types, supporting a wide range of data types, such as text, numbers, files, and relational data. Custom fields provide flexibility for handling unique data formats, and field arguments like `read_only`, `default`, and `validators` offer fine control over how data is processed.
