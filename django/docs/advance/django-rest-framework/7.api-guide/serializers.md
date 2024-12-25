# Django REST Framework: Serializers

---

## **Key Serializers**

---

### 1. **Serializer**

- **Description**: Base class to define how data is converted between native Python types and JSON or other formats.

  **Example**:

  ```python
  from rest_framework import serializers

  class MySerializer(serializers.Serializer):
      name = serializers.CharField(max_length=100)
      age = serializers.IntegerField()
  ```

---

### 2. **ModelSerializer**

- **Description**: A shortcut to create serializers for Django models, automatically generating fields based on model attributes.

  **Example**:

  ```python
  from rest_framework import serializers
  from myapp.models import MyModel

  class MyModelSerializer(serializers.ModelSerializer):
      class Meta:
          model = MyModel
          fields = ['name', 'age']
  ```

---

## **Validation**

### **1. Field-Level Validation**

- **Description**: Validates individual fields using methods like `validate_<fieldname>()`. This is ideal for simple checks on single fields.

  **Example**:

  ```python
  def validate_age(self, value):
      if value < 18:
          raise serializers.ValidationError("Age must be at least 18.")
      return value
  ```

---

### **2. Object-Level Validation**

- **Description**: Validates multiple fields by overriding the `validate()` method. This is useful for inter-field validation.

  **Example**:

  ```python
  def validate(self, data):
      if data['start'] > data['end']:
          raise serializers.ValidationError("End date must be after the start date.")
      return data
  ```

---

### **3. Cross-Field Validation**

- **Description**: Checks that multiple fields have related values (e.g., matching passwords).

  **Example**:

  ```python
  class RegistrationSerializer(serializers.Serializer):
      password = serializers.CharField(write_only=True)
      confirm_password = serializers.CharField(write_only=True)

      def validate(self, data):
          if data['password'] != data['confirm_password']:
              raise serializers.ValidationError("Passwords must match.")
          return data
  ```

---

### **4. Conditional Validation**

- **Description**: Validates fields based on conditions (e.g., validating one field depending on another's value).

  **Example**:

  ```python
  class BookingSerializer(serializers.Serializer):
      booking_type = serializers.ChoiceField(choices=['free', 'paid'])
      payment_method = serializers.CharField(required=False)

      def validate(self, data):
          if data['booking_type'] == 'paid' and not data.get('payment_method'):
              raise serializers.ValidationError("Payment method is required for paid bookings.")
          return data
  ```

---

### **5. Validation with `ModelSerializer`**

- **Description**: When using `ModelSerializer`, Django model validation rules (e.g., unique, max_length) are applied automatically. You can add custom validation if needed.

  **Example**:

  ```python
  class UserSerializer(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ['username', 'email']

      def validate_email(self, value):
          if "spam" in value:
              raise serializers.ValidationError("Email cannot contain 'spam'.")
          return value
  ```

---

### **6. Validation in Nested Serializers**

- **Description**: Validates fields in nested relationships using the parent serializer.

  **Example**:

  ```python
  class ProfileSerializer(serializers.Serializer):
      bio = serializers.CharField()
      website = serializers.URLField(required=False)

  class UserSerializer(serializers.Serializer):
      username = serializers.CharField(max_length=100)
      profile = ProfileSerializer()

      def validate_profile(self, value):
          if 'http' not in value.get('website', ''):
              raise serializers.ValidationError("Invalid website URL.")
          return value
  ```

---

### **7. Custom ValidationError Messages**

- **Description**: You can customize error messages using the `error_messages` argument.

  **Example**:

  ```python
  class ProductSerializer(serializers.Serializer):
      price = serializers.DecimalField(max_digits=10, decimal_places=2, error_messages={
          'max_digits': 'Price cannot exceed 10 digits.',
          'decimal_places': 'Price must have 2 decimal places.'
      })
  ```

---

## **Deserialization and Save**

- **Description**: Serializers handle deserialization and saving to the database using `.save()`.

  **Example**:

  ```python
  serializer = MyModelSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
  ```

---

## **Conclusion**

Validation in Django REST Framework offers robust mechanisms to ensure data integrity. Field-level validation, object-level validation, cross-field validation, and custom error messages allow for comprehensive input checking. `ModelSerializer` provides automatic validation using Django's built-in model fields, while nested serializers help validate related fields in complex data structures.
