# Python Basics - Conditionals and Recursion

In Python, conditionals and recursion are used to control the flow of a program based on conditions and to solve problems that require repeated applications of the same process.

## 1. Conditionals

Conditionals allow the program to execute certain blocks of code based on whether a condition is true or false.

- **if statement**: Executes a block of code if a condition is true.
- **else statement**: Executes a block of code if the condition in the `if` statement is false.
- **elif statement**: Adds additional conditions after an initial `if` statement.

### Example Code:

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

### Use Cases:

- **if-else**: Making decisions based on user input, such as checking passwords or determining game logic.

---

## 2. Recursion

Recursion is a programming technique where a function calls itself to solve a problem that can be broken down into smaller instances of the same problem.

- **Base case**: The condition that stops the recursion.
- **Recursive case**: The part of the function where it calls itself.

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

- **Recursion**: Solving problems like calculating factorials, navigating directories, or performing tree traversals.

---

### Summary:

In this chapter, we explored:

1. **Conditionals**: Using `if`, `else`, and `elif` to control program flow based on conditions.
2. **Recursion**: Breaking down problems by having functions call themselves.
