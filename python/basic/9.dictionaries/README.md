# Python Basics - Dictionaries

Dictionaries are a powerful and versatile data type in Python, often used for mapping keys to values. This chapter explores dictionaries, their properties, operations, and various ways they can be utilized. Below is a summary of the key concepts covered in Chapter 11.

---

## 1. A Dictionary Is a Mapping

A dictionary in Python is a collection of key-value pairs, where each key maps to a corresponding value. Unlike lists, which have integer indices, dictionary keys can be of almost any data type.

### Example Code:

```python
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp['two'])
```

### Result:

```
dos
```

### Use Cases:

- Storing and retrieving data based on unique keys.
- Creating lookup tables for quick data access.

---

## 2. Dictionary as a Collection of Counters

Dictionaries can be used to count occurrences of items in a collection. This method is efficient because you only store keys that actually appear.

### Example Code:

```python
def histogram(s):
d = dict()
for c in s:
d[c] = d.get(c, 0) + 1
return d

result = histogram('brontosaurus')
print(result)
```

### Result:

```
{'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
```

### Use Cases:

- Counting character frequency in a string.
- Counting occurrences of items in a list or dataset.

---

## 3. Looping and Dictionaries

You can loop through a dictionary to access its keys and values. This is particularly useful for processing or displaying dictionary contents.

### Example Code:

```python
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
for key, value in eng2sp.items():
print(f"{key} => {value}")
```

### Result:

```
one => uno
two => dos
three => tres
```

### Use Cases:

- Iterating over key-value pairs for processing or transformations.
- Displaying contents of a dictionary in a readable format.

---

## 4. Reverse Lookup

A reverse lookup involves finding the key associated with a particular value in a dictionary. Since there might be multiple keys for the same value, this operation can be less efficient.

### Example Code:

```python
def reverse_lookup(d, v):
for k in d:
if d[k] == v:
return k
raise LookupError('Value does not appear in the dictionary')

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
result = reverse_lookup(eng2sp, 'tres')
print(result)
```

### Result:

```
three
```

### Use Cases:

- Finding keys when only the value is known.
- Useful in situations where values are unique and reverse mapping is required.

---

## 5. Dictionaries and Lists

Lists can be stored as values in dictionaries, but not as keys since keys must be hashable (immutable). This combination allows for more complex data structures.

### Example Code:

```python
def invert_dict(d):
inverse = dict()
for key in d:
val = d[key]
inverse.setdefault(val, []).append(key)
return inverse

hist = {'a': 2, 'b': 3, 'c': 2}
inverse = invert_dict(hist)
print(inverse)
```

### Result:

```
{2: ['a', 'c'], 3: ['b']}
```

### Use Cases:

- Inverting a dictionary to map values to keys.
- Grouping keys by their corresponding values.

---

## 6. Memos

Memoization is a technique where previously computed values are stored in a dictionary to avoid redundant calculations, significantly improving performance for recursive functions.

### Example Code:

```python
known = {0: 0, 1: 1}

def fibonacci(n):
if n in known:
return known[n]
res = fibonacci(n - 1) + fibonacci(n - 2)
known[n] = res
return res

result = fibonacci(10)
print(result)
```

### Result:

```
55
```

### Use Cases:

- Optimizing recursive functions by storing intermediate results.
- Reducing computation time in algorithms with overlapping subproblems.

---

## 7. Global Variables

Global variables can be accessed from any function, but modifying them requires the \`global\` keyword. They should be used sparingly to avoid making the code difficult to debug.

### Example Code:

```python
count = 0

def increment():
global count
count += 1

increment()
increment()
print(count)
```

### Result:

```
2
```

### Use Cases:

- Maintaining state or counters across multiple function calls.
- Configuring settings accessible throughout the program.

---

### Summary:

This chapter provided an in-depth exploration of dictionaries in Python. From their basic definition as mappings to their use in memoization and reverse lookups, dictionaries are shown to be a versatile tool in any Python programmer's toolkit. Understanding how to effectively create, manipulate, and utilize dictionaries is essential for writing efficient and readable code.
