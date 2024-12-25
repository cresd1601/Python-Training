# Python Basics - Fruitful Functions

In this chapter, we delve into fruitful functions in Python—functions that return a value.

## 1. What is a Fruitful Function?

A fruitful function is a function that computes and returns a value using the `return` statement. Unlike void functions that only perform actions, fruitful functions yield output that can be stored, used in further computations, or printed.

### Example Code:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

### Use Cases:

- **Fruitful functions**: Commonly used in calculations, returning values from APIs, or providing outputs based on user input.

---

## 2. Composition

Fruitful functions can be combined, or **composed**, where one function's output becomes the input to another.

### Example Code:

```python
def square(x):
    return x * x

def add_and_square(a, b):
    return square(add(a, b))

print(add_and_square(2, 3))  # Output: 25
```

### Use Cases:

- **Composition**: Simplifies complex calculations by breaking them into smaller, reusable functions.

---

## 3. Recursion in Fruitful Functions

Recursion is often used in fruitful functions to solve problems that involve breaking the problem down into smaller sub-problems.

### Example Code:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Use Cases:

- **Recursion**: Used in mathematical computations such as factorials, Fibonacci sequences, and divide-and-conquer algorithms.

---

### Summary:

In this chapter, we covered:

1. **Fruitful functions**: Functions that return values.
2. **Composition**: Combining functions to simplify computations.
3. **Recursion in fruitful functions**: Using recursion to solve complex problems with smaller instances.
