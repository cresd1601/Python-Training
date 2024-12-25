# Python Basics - Files

Mastering file handling, including reading and writing files, managing exceptions, and working with databases, is essential for Python programmers looking to develop more sophisticated and persistent applications.

---

## 1. Persistence

Persistence refers to the ability of a program to save data between runs. Programs that store data permanently on disk are considered persistent. This chapter emphasizes the difference between transient programs, which lose data after execution, and persistent ones, which retain data in files or databases.

### Use Cases:

- Operating systems and web servers that need to maintain data or state over time.

---

## 2. Reading and Writing Files

Python makes it easy to work with text files. You can open a file in read or write mode, and perform operations like reading lines or writing data.

### Example Code:

```python
fout = open('output.txt', 'w')
fout.write("This here's the wattle,\n")
fout.write("the emblem of our land.\n")
fout.close()
```

### Result:

A new file `output.txt` is created with the text written line by line.

### Use Cases:

- Saving program output to a file.
- Reading configuration files.

---

## 3. Format Operator

The format operator `%` is used for formatting strings, particularly when writing non-string data to a file. The format string can include format sequences like `%d` for integers.

### Example Code:

```python
camels = 42
'In %d years I have spotted %d camels.' % (3, camels)
```

### Result:

```
'In 3 years I have spotted 42 camels.'
```

### Use Cases:

- Formatting output before writing to a file.
- Embedding variables within strings.

---

## 4. Filenames and Paths

Files are organized into directories, and Python’s `os` module provides tools to work with these directories and file paths. Paths can be relative or absolute.

### Example Code:

```python
import os
cwd = os.getcwd()
```

### Result:

```
'/home/user'
```

### Use Cases:

- Navigating the file system in scripts.
- Managing file locations dynamically.

---

## 5. Catching Exceptions

When working with files, many things can go wrong (e.g., file not found, permission denied). Python handles these errors using exceptions, specifically the `try` and `except` blocks.

### Example Code:

```python
try:
    fin = open('bad_file')
except:
    print('Something went wrong.')
```

### Result:

Prints a message if the file cannot be opened.

### Use Cases:

- Gracefully handling file access errors.
- Debugging file-related issues in scripts.

---

## 6. Databases

Python allows you to use simple databases that persist data like dictionaries, using the `dbm` module. This is particularly useful when dealing with large amounts of structured data.

### Example Code:

```python
import dbm
db = dbm.open('captions', 'c')
db['cleese.png'] = 'Photo of John Cleese.'
db.close()
```

### Result:

Creates a simple database where keys and values are stored persistently.

### Use Cases:

- Storing large datasets in a persistent manner.
- Using a lightweight database for applications.

---

## 7. Pickling

The `pickle` module serializes Python objects into a byte stream, which can be stored in a file or a database. This is useful for storing complex data types that go beyond simple strings or numbers.

### Example Code:

```python
import pickle
t = [1, 2, 3]
s = pickle.dumps(t)
t2 = pickle.loads(s)
```

### Result:

Serializes the list `t` and then deserializes it back to its original form.

### Use Cases:

- Saving and restoring complex data structures.
- Storing non-string data in databases.

---

## 8. Pipes

Pipes allow Python programs to interact with other programs on the operating system. This can be used to execute shell commands or run other applications.

### Example Code:

```python
import os
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
```

### Result:

Executes the `ls -l` command and reads its output in Python.

### Use Cases:

- Running system commands from a Python script.
- Automating tasks that require shell access.

---

### Summary:

Chapter 14 of _Think Python_ provides a deep dive into file handling, covering essential concepts like reading and writing files, handling exceptions, and using databases. These are crucial skills for any Python programmer, enabling them to build more complex, persistent applications.
