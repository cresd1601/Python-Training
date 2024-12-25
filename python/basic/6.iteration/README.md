# Python Basics - Iteration

In this chapter, we explore **iteration** in Python, which allows us to repeat actions multiple times. Python provides several ways to implement iteration using loops.

## 1. For Loops

The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each element in the sequence.

### Example Code:

```python
for i in range(5):
    print(i)
```

### Use Cases:

- **for loop**: Useful for iterating over collections of data, such as processing lists or strings.

---

## 2. While Loops

The `while` loop continues to execute a block of code as long as the condition remains true.

### Example Code:

```python
n = 5
while n > 0:
    print(n)
    n -= 1
```

### Use Cases:

- **while loop**: Useful for repeating tasks when the number of iterations is not known beforehand, such as waiting for user input or monitoring a condition.

---

## 3. Break and Continue

The `break` statement is used to exit a loop prematurely, while the `continue` statement skips the rest of the code inside the loop for the current iteration.

### Example Code:

```python
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

### Use Cases:

- **break**: Stopping a loop based on a condition, such as ending early in a search.
- **continue**: Skipping certain iterations in the loop, such as avoiding invalid data.

---

### Summary:

In this chapter, we covered:

1. **For Loops**: Iterating over sequences of data.
2. **While Loops**: Repeating code as long as a condition is true.
3. **Break and Continue**: Controlling the flow of loops by stopping or skipping iterations.
