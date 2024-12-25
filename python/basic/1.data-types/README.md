# Python Basics - Values and Types

In Python, values are classified into different types, each serving a specific purpose. Below is a brief explanation and example code for each data type category, along with real-world use cases.

## 1. Numeric Data Types

Numeric types represent numbers in various forms.

- **int**: Whole numbers, e.g., `3`, `100`. Commonly used for counting.
- **float**: Decimal values, e.g., `3.14`. Used in precise calculations.
- **complex**: Numbers with real and imaginary parts, e.g., `1 + 2j`.

### Example Code:

```python
int_val = 42
float_val = 9.99
complex_val = 3 + 4j
```

### Use Cases:

- **int**: Counting items.
- **float**: Measuring quantities.
- **complex**: Engineering simulations.

---

## 2. Sequence Types

Sequence types represent ordered collections of items.

- **list**: Mutable collection, e.g., `['apple', 'banana']`.
- **tuple**: Immutable collection, e.g., `(10, 20)`.
- **range**: Represents a range of numbers.

### Example Code:

```python
list_val = ['apple', 'banana']
tuple_val = (10, 20)
range_val = range(1, 4)
```

### Use Cases:

- **list**: Managing dynamic collections.
- **tuple**: Storing constant data.
- **range**: Looping through a sequence.

---

## 3. String Data Types

Strings represent text.

- **str**: Sequence of characters, e.g., `"Hello, World!"`.

### Example Code:

```python
str_val = "Hello!"
```

### Use Cases:

- **str**: Storing text input.

---

## 4. Binary Data Types

Binary types work with raw bytes.

- **bytes**: Immutable, e.g., `b'Hello'`.
- **bytearray**: Mutable sequence of bytes.

### Example Code:

```python
bytes_val = b"Hello"
bytearray_val = bytearray([255, 128])
```

### Use Cases:

- **bytes**: Network communication.
- **bytearray**: Modifying binary data.

---

## 5. Mapping Data Type

Mapping types store key-value pairs.

- **dict**: Stores key-value pairs, e.g., `{"name": "John"}`.

### Example Code:

```python
dict_val = {"name": "John", "age": 30}
```

### Use Cases:

- **dict**: Storing structured data.

---

## 6. Boolean Type

Boolean types represent truth values.

- **bool**: `True` or `False`.

### Example Code:

```python
is_active = True
```

### Use Cases:

- **bool**: Controlling logic flow.

---

## 7. Set Data Types

Set types store unique items.

- **set**: Mutable, e.g., `{1, 2, 3}`.
- **frozenset**: Immutable version of a set.

### Example Code:

```python
set_val = {1, 2, 3}
```

### Use Cases:

- **set**: Removing duplicates.

---

### Summary:

We covered seven fundamental types in Python:

1. **Numeric types**: `int`, `float`, `complex`
2. **Sequence types**: `list`, `tuple`, `range`
3. **String types**: `str`
4. **Binary types**: `bytes`, `bytearray`
5. **Mapping types**: `dict`
6. **Boolean types**: `bool`
7. **Set types**: `set`, `frozenset`
