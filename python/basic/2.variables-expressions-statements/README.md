# Python Basics - Variables, Expressions, and Statements

In Python, variables, expressions, and statements form the foundation of programming. This chapter focuses on how to store data, compute values, and build meaningful code structures.

## 1. Variables

A variable is a name that refers to a value. Variables allow you to store data and reuse it throughout your program.

- **Assignment Statement**: Used to assign a value to a variable. The syntax is `variable_name = value`.
- **Naming Rules**: Variable names can contain letters, numbers, and underscores but must not start with a number.

### Example Code:

```python
message = 'Hello, World!'
number = 42
pi = 3.14159

print(message)  # Output: Hello, World!
print(number)   # Output: 42
print(pi)       # Output: 3.14159
```

### Use Cases:

- Storing and manipulating user input.
- Saving computation results for later use in a program.

---

## 2. Expressions and Statements

An expression is a combination of values, variables, and operators that produces a result. A statement is a unit of code that performs an action, such as assigning a value to a variable or printing a result.

- **Expression**: Combines values and operators, e.g., `2 + 2`, `x * y`.
- **Statement**: A complete line of code that performs an action, e.g., `print(42)` or `x = y + 1`.

### Example Code:

```python
x = 5
y = 3
result = x + y  # Expression: x + y
print(result)   # Statement: printing the result
```

### Use Cases:

- Evaluating mathematical formulas or logical comparisons.
- Controlling the flow of the program using expressions inside conditionals and loops.

---

## 3. Script Mode vs. Interactive Mode

Python can be run in two modes:

- **Interactive Mode**: You type commands and execute them immediately in the Python shell.
- **Script Mode**: You write code in a file and run the entire file as a program.

### Example Code (Script Mode):

```python
# Save this code to a file called my_script.py and run it
x = 10
y = 20
print(x + y)  # Output: 30
```

### Use Cases:

- Interactive mode is useful for testing and experimenting with short pieces of code.
- Script mode is best for writing larger programs and automating tasks.

---

## 4. Order of Operations

When expressions contain multiple operators, Python follows the standard order of operations (PEMDAS):

- **Parentheses**
- **Exponentiation**
- **Multiplication and Division**
- **Addition and Subtraction**

### Example Code:

```python
result = (2 + 3) * 4  # Parentheses first, then multiplication
print(result)  # Output: 20
```

### Use Cases:

- Ensuring correct evaluation of mathematical expressions in programs.
- Grouping operations to control the order in which they are executed.

---

## 5. Comments

Comments are used to explain the purpose of code and make the program easier to understand. They are ignored by the Python interpreter.

- **Single-line Comment**: Starts with `#`.
- **Multi-line Comment**: You can use triple quotes `'''` or `"""` for longer explanations.

### Example Code:

```python
# This is a single-line comment
x = 5  # Assigning 5 to variable x

'''
This is a
multi-line comment
explaining the code in detail.
'''
```

### Use Cases:

- Adding explanations for complex logic.
- Documenting sections of code for future reference.

---

### Summary:

In this lesson, we covered the following foundational topics in Python:

1. **Variables**: Storing data using meaningful names.
2. **Expressions and Statements**: Combining values and operators to produce results and take actions.
3. **Script vs. Interactive Mode**: Writing and executing Python code in different modes.
4. **Order of Operations**: Understanding the precedence of operators in expressions.
5. **Comments**: Using comments to explain code and improve readability.
