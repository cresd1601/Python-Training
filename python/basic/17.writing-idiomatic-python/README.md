# Chapter 1: Control Structures and Functions

## 1.1 If Statements

### 1.1.1 Use if statements to return early on error conditions

When writing functions, it's often better to check for error conditions at the start and return immediately if any are found. This keeps the "normal" code path at the outermost level of indentation, improving readability.

**Example:**

```python
# Harmful
def process_login_form(request):
    if request.form.get('username') and request.form.get('password'):
        if captcha_displayed(request) and captcha_passed(request):
            if authenticate_user(request.form['username'], request.form['password']):
                current_user.login()
                return redirect(HOME_PAGE)
            else:
                return 'Unable to authenticate with provided username and password', 403
        else:
            if captcha_displayed(request):
                return 'Captcha entry failed. Please resubmit', 403
            else:
                return 'Missing username or password. Both are required', 400

# Idiomatic
def process_login_form(request):
    if 'username' not in request.form:
        return 'Please enter a value for username', 400
    if 'password' not in request.form:
        return 'Please enter a value for password', 400
    if captcha_displayed(request) and not captcha_passed(request):
        return 'Captcha entry failed. Please resubmit', 403
    if not authenticate_user(request.form['username'], request.form['password']):
        return 'Unable to authenticate with provided username and password', 403
    current_user.login()
    return redirect(HOME_PAGE)
```

### 1.1.2 Chain comparisons to make if statements more concise

Python allows chaining comparisons for concise and readable code.

**Example:**

```python
# Harmful
if x <= y and y <= z:
    return True

# Idiomatic
if x <= y <= z:
    return True
```

...

# Chapter 2: Working with Data

## 2.1 Variables

### 2.1.1 Use multiple assignment to condense variables all set to the same value

Python supports multiple assignment, which can make your code more concise and readable.

**Example:**

```python
# Harmful
x = 'foo'
y = 'foo'
z = 'foo'

# Idiomatic
x = y = z = 'foo'
```

### 2.1.2 Avoid using a temporary variable when performing a swap of two values

You can use Python's tuple unpacking to swap values without needing a temporary variable.

**Example:**

```python
# Harmful
foo = 'Foo'
bar = 'Bar'
temp = foo
foo = bar
bar = temp

# Idiomatic
foo = 'Foo'
bar = 'Bar'
(foo, bar) = (bar, foo)
```

...

# Chapter 3: Organizing Your Code

## 3.1 Formatting

### 3.1.1 Use all capital letters when declaring global constant values

Use uppercase letters to denote constant values to make your code clearer and to signal to other developers that these values should not change.

**Example:**

```python
MAX_CONNECTIONS = 10
TIMEOUT = 120
```

### 3.1.2 Format your code according to PEP8

Following PEP8, Python's style guide, ensures that your code is consistent with most Python codebases.

**Example:**

```python
# PEP8 recommends:
def long_function_name(var_one, var_two, var_three,
                       var_four):
    print(var_one)
```

...

# Chapter 4: General Advice

## 4.1 Avoid Reinventing the Wheel

### 4.1.1 Get to Know PyPI (The Python Package Index)

PyPI is a vast repository of Python packages that can save you significant development time by providing ready-made solutions. Before implementing a solution from scratch, always check PyPI to see if a library already exists for your needs.

**Example:**
Instead of writing a function to parse JSON, use the `json` library available in Python's standard library.

```python
import json

data = '{"name": "John", "age": 30}'
parsed_data = json.loads(data)
print(parsed_data)
```

### 4.1.2 Learn the Contents of the Python Standard Library

The Python Standard Library is extensive, offering modules and packages that cover many programming needs. Familiarizing yourself with these can prevent you from unnecessarily reimplementing features that already exist.

**Example:**
When working with file paths, use `os.path` instead of manually manipulating strings.

```python
import os

current_directory = os.getcwd()
file_name = 'example.txt'
file_path = os.path.join(current_directory, file_name)
print(file_path)
```

...

### 4.2 Modules of Note

### 4.2.1 Learn the Contents of the itertools Module

The `itertools` module provides tools for handling iterators, making it easier to work with looping and iteration in Python. This module is often the answer to common questions about missing functionality in Python's core.

**Example:**
Using `itertools.chain` to iterate over multiple lists as if they were a single list.

```python
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in itertools.chain(list1, list2):
    print(item)
```

### 4.2.2 Use Functions in the os.path Module When Working with Directory Paths

The `os.path` module is designed to handle common file path operations, reducing the risk of errors and making your code more portable.

**Example:**
Creating a backup of a file using `os.path` to manage file paths.

```python
import os
from datetime import date

current_directory = os.getcwd()
file_name = 'data.txt'
backup_name = os.path.splitext(file_name)[0] + '.bak'
backup_directory = os.path.join(current_directory, 'backups')
today = date.today()
backup_path = os.path.join(backup_directory, str(today))

if not os.path.exists(backup_path):
    os.makedirs(backup_path)

os.rename(os.path.join(current_directory, file_name), os.path.join(backup_path, backup_name))
```

## 4.3 Testing

### 4.3.1 Use an Automated Testing Tool; It Doesn’t Matter Which One

Automated tests are crucial for maintaining code quality. While many tools are available, the important thing is to choose one and use it consistently.

**Example:**
Using `unittest` from Python's standard library to create a simple test case.

```python
import unittest

def add(a, b):
    return a + b

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

### 4.3.2 Separate Your Test Code from Your Application Code

Keeping your test code separate from your application code ensures a clean codebase and makes it easier to manage tests.

**Example:**
Organize your project structure as follows:

```
project/
│
├── my_module.py
└── tests/
    └── test_my_module.py
```

### 4.3.3 Use Unit Tests to Aid in Refactoring

Unit tests are invaluable when refactoring code because they help ensure that changes don’t introduce new bugs.

**Example:**
If you're refactoring a function, first write unit tests to cover its current behavior. Then, after refactoring, run these tests to confirm the function still works as expected.

```python
def multiply(a, b):
    return a * b

class TestMath(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)

# After refactoring:
def multiply(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result
```

### 4.3.4 Make Use of the Appropriate Assert Methods in Unit Tests

Python’s `unittest` module provides a variety of assert methods. Using the most appropriate assert method makes your tests more clear and specific.

**Example:**
Instead of using `assertTrue(a == b)`, use `assertEqual(a, b)` to compare values directly.

```python
class TestMath(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(10, 10)
```
