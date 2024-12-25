# Python Basics - Strings

This chapter focuses on working with **strings** in Python, which represent sequences of characters. Strings are one of the most commonly used data types in Python.

## 1. String Methods

Python provides several built-in methods for manipulating strings, such as changing their case, splitting them, and checking their content.

### Example Code:

```python
message = "Hello, World!"
print(message.upper())  # Output: HELLO, WORLD!
print(message.lower())  # Output: hello, world!
print(message.startswith("Hello"))  # Output: True
```

### Use Cases:

- **String methods**: Useful for formatting text, validating input, or extracting information from strings.

---

## 2. String Slicing

String slicing allows you to extract a substring from a string by specifying a range of indices.

### Example Code:

```python
message = "Hello, World!"
print(message[0:5])  # Output: Hello
print(message[-6:])  # Output: World!
```

### Use Cases:

- **String slicing**: Often used to extract specific parts of a string, such as file extensions, substrings, or individual characters.

---

## 3. String Concatenation

You can concatenate (combine) strings using the `+` operator or by joining them together.

### Example Code:

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

### Use Cases:

- **String concatenation**: Used to combine multiple strings, such as user inputs or parts of a message.

---

## 4. Formatting Strings

Python provides several ways to format strings, including using f-strings, `str.format()`, and concatenation.

### Example Code:

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.
```

### Use Cases:

- **String formatting**: Useful for generating dynamic content, such as user prompts, reports, and logging messages.

---

### Summary:

In this chapter, we covered:

1. **String Methods**: Using built-in methods to manipulate strings.
2. **String Slicing**: Extracting specific portions of a string.
3. **String Concatenation**: Combining strings into one.
4. **Formatting Strings**: Inserting variables into strings for dynamic outputs.
