# Python Classes and Objects

## What is a Class?

A class is like a blueprint that we use to create objects.

For example, a `Student` class can be used to create different student objects. Each student can have their own name and other information.

## Example

```python
class Student:
    name: str

    def set_name(self, NAME):
        self.name = NAME

    def get_name(self):
        return self.name


student = Student()

student.set_name("saad")

name = student.get_name()

print(name)
```

**Output:**

```text
saad
```

## Understanding the Code

### 1. Creating a Class

```python
class Student:
```

Here, we are creating a class named `Student`.

This class will act as a blueprint for creating student objects.

### 2. Declaring a Variable

```python
name: str
```

Here, we are declaring a variable named `name` with a type hint of `str`.

It tells developers that the `name` variable is expected to contain a string.

### 3. Creating a Method to Set the Name

```python
def set_name(self, NAME):
    self.name = NAME
```

Here, we are creating a method named `set_name()`.

- `self` refers to the current object.
- `NAME` is the value that we receive as an argument.
- `self.name = NAME` stores that value inside the object's `name` variable.

### 4. Creating a Method to Get the Name

```python
def get_name(self):
    return self.name
```

Here, we are creating another method named `get_name()`.

It returns the value stored inside the object's `name` variable.

### 5. Creating an Object

```python
student = Student()
```

Here, we are creating an object of the `Student` class.

Now we can access the methods and variables of this class using the `student` object.

### 6. Setting the Name

```python
student.set_name("saad")
```

Here, we are calling the `set_name()` method and passing `"saad"` as an argument.

This will store `"saad"` inside `student.name`.

### 7. Getting the Name

```python
name = student.get_name()
```

Here, we are calling the `get_name()` method.

It returns the name stored inside the object, and we store that returned value inside the `name` variable.

### 8. Printing the Name

```python
print(name)
```

Finally, we print the name stored inside the `name` variable.

**Output:**

```text
saad
```

## Important Things to Remember

- **Class:** A blueprint used to create objects.
- **Object:** An instance of a class.
- **Attribute:** A variable that belongs to an object, like `self.name`.
- **Method:** A function defined inside a class.
- **self:** Refers to the current object.
- **set_name():** Used to store a name.
- **get_name():** Used to retrieve a name.

**In simple words:** A class helps us organize related variables and functions together. We create objects from a class and use those objects to access its variables and methods.