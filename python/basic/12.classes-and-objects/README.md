# Python Basics - Classes and Objects

This chapter explores the fundamental concepts of object-oriented programming (OOP) in Python. It introduces the idea of creating programmer-defined types, working with attributes, and understanding the mutability of objects. Below is a summary of the key concepts covered in Chapter 15.

---

## 1. Programmer-Defined Types

In Python, you can create your own types, known as classes. A class defines a new type of object, which can have its own attributes and methods.

### Example Code:

```python
class Point:
    # Represents a point in 2-D space.
    pass
```

### Use Cases:

- Defining custom data structures that closely model real-world entities.
- Encapsulating related data and functions within a single class.

---

## 2. Attributes

Attributes are variables that belong to an instance of a class. They are accessed using dot notation.

### Example Code:

```python
blank = Point()
blank.x = 3.0
blank.y = 4.0
```

### Use Cases:

- Storing and managing state information within an object.
- Representing characteristics or properties of an object.

---

## 3. Instances as Return Values

Functions can return instances of a class, allowing for the creation and manipulation of objects within a function.

### Example Code:

```python
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p
```

### Use Cases:

- Generating new objects based on calculations or transformations of existing ones.
- Modularizing code by returning objects from functions.

---

## 4. Objects Are Mutable

Objects in Python are mutable, meaning their attributes can be changed after the object is created.

### Example Code:

```python
box.width = box.width + 50
box.height = box.height + 100
```

### Use Cases:

- Modifying the state of an object over time.
- Implementing methods that alter the attributes of an object.

---

## 5. Copying

Copying an object creates a new object with the same attributes. However, a shallow copy does not copy embedded objects, leading to shared references between the original and the copy.

### Example Code:

```python
import copy
p2 = copy.copy(p1)
```

### Use Cases:

- Creating duplicates of objects while managing shared references.
- Preventing unintended modifications by copying objects before changing them.

---

### Summary:

Understanding classes and objects is crucial for effective Python programming, particularly in developing applications that model real-world entities. This chapter lays the groundwork for more advanced object-oriented concepts by introducing the basics of defining and working with custom types in Python.
