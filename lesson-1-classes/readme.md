# Understanding Classes and Objects in Python

## 1. What are Objects?

Real-world things can be represented as objects in programming.

Objects occupy memory, and objects are useful because they can store data and perform operations.

Objects contain:
- Variables (to store values)
- Methods (to perform operations)

Variables inside objects store values, while methods inside objects perform operations.

---

## 2. How Do We Access Variables Inside Objects?

Suppose we have an object with a variable called `name`.

Now we want to give a value to this variable `name`, which is inside the object.

We can use a method to give or set the value to the variable `name`.

This method is called a **Setter**.

Setters are methods used to give values to variables inside an object.

---

## 3. What are Getters?

Suppose the `name` variable has a value (`"saad"`) that we gave using a setter method.

Now we want to access or get the value of the `name` variable.

For this, we can use another method called `get_name()` to get the value of the variable.

This method is called a **Getter**.

Getters are methods used to get or access the values of variables inside an object.

---

## 4. What Do Objects Contain?

Inside objects, we have variables that store values and methods.

Methods can be used to:
- Set values inside objects.
- Get values from objects.
- Perform operations using the values stored inside objects.

So:

- Variables store values inside objects.
- Setter methods are used to give values to variables inside objects.
- Getter methods are used to get values from variables inside objects.

---

## 5. How Do We Create Objects?

To create objects, we define classes.

A class defines the structure of how our objects will look and what they will contain.

For example, we can create a class called `Student` with:

- A variable called `name`.
- A method called `get_name()`.
- A method called `set_name()`.

These methods will be used to set and get the value of the variable `name`.

Then we can create an object from this class.

The object will have the variables and methods that we defined in the class.

We first create objects of the class, then give values to the variables inside those objects, and then access those values.

---

## 6. Code Example 1 — Using Setters and Getters

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

### Output

```text
saad
```

---

## 7. Understanding the Flow of Code 1

1. We create a class called `Student`.
2. Inside the class, we define a variable called `name`.
3. We define a setter method called `set_name()` to give a value to the `name` variable.
4. We define a getter method called `get_name()` to get the value of the `name` variable.
5. We create an object called `student` from the `Student` class.
6. We call `student.set_name("saad")` to set the value of the `name` variable.
7. We call `student.get_name()` to get the value of the `name` variable.
8. Finally, we print the value.

---

## 8. What is a Constructor?

In the previous example, we created an object first and then used a setter method to give values to its variables.

But what if we want to give values to the variables at the time of creating the object?

For this purpose, we use a special method called a **Constructor**.

In Python, the constructor-like initialization method is called:

```python
__init__()
```

The `__init__()` method automatically runs when we create an object of a class.

It is used to initialize the object's variables with values.

Instead of creating an object first and then calling a setter, we can directly pass values while creating the object.

---

## 9. How Does `__init__()` Work?

Suppose we have a `Student` class with two variables:

- `name`
- `age`

We want to give values to these variables when we create the object.

We can define an `__init__()` method that accepts these values and assigns them to the object's variables.

```python
class Student:
    name: str
    age: int

    def __init__(self, NAME, AGE):
        self.name = NAME
        self.age = AGE
```

### Understanding the Code

- `__init__()` automatically runs when an object is created.
- `NAME` receives the name passed during object creation.
- `AGE` receives the age passed during object creation.
- `self.name = NAME` stores the name inside the object.
- `self.age = AGE` stores the age inside the object.

---

## 10. Creating Objects Using a Constructor

Now we can create an object and pass values directly to it.

```python
student = Student(NAME="saad", AGE=20)
```

When this line executes:

1. Python creates a new object of the `Student` class.
2. Python automatically calls the `__init__()` method.
3. `"saad"` is passed to `NAME`.
4. `20` is passed to `AGE`.
5. The values are stored inside the object.

Now the object contains:

| Variable | Value |
|---|---|
| `name` | `"saad"` |
| `age` | `20` |

We no longer need to call separate setter methods to initialize these values.

---

## 11. Using Getters to Access Object Variables

We can create getter methods to access the variables inside our object.

```python
def get_name(self):
    return self.name

def get_age(self):
    return self.age
```

- `get_name()` returns the name stored inside the object.
- `get_age()` returns the age stored inside the object.

For example:

```python
name = student.get_name()
age = student.get_age()

print("Name=", name)
print("Age=", age)
```

### Output

```text
Name= saad
Age= 20
```

---

## 12. Returning Multiple Values From a Method

What if we want to get both the name and age using a single method?

Instead of creating two separate getter methods and calling them individually, we can create a method that returns both values.

```python
def get_name_and_age(self):
    return self.name, self.age
```

This method returns both the `name` and `age`.

We can receive these values in two different variables:

```python
name, age = student.get_name_and_age()
```

Python automatically unpacks the returned values into the variables.

- `name` receives the first value.
- `age` receives the second value.

This is called **Multiple Assignment / Unpacking**.

---

## 13. Code Example 2 — Using Constructors and Multiple Return Values

```python
class Student:
    name: str
    age: int

    def __init__(self, NAME, AGE):
        self.name = NAME
        self.age = AGE

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_name_and_age(self):
        return self.name, self.age


student = Student(NAME="saad", AGE=20)

name, age = student.get_name_and_age()

print("Name=", name)
print("Age=", age)
```

### Output

```text
Name= saad
Age= 20
```

---

## 14. Understanding the Flow of Code 2

1. We create a class called `Student`.
2. We define two variables: `name` and `age`.
3. We define the `__init__()` method.
4. The `__init__()` method receives `NAME` and `AGE` when the object is created.
5. We assign `NAME` to `self.name`.
6. We assign `AGE` to `self.age`.
7. We define `get_name()` to return the student's name.
8. We define `get_age()` to return the student's age.
9. We define `get_name_and_age()` to return both the name and age.
10. We create an object by passing `NAME="saad"` and `AGE=20`.
11. The constructor automatically executes and stores the values inside the object.
12. We call `get_name_and_age()` to retrieve both values.
13. Python unpacks the returned values into `name` and `age`.
14. Finally, we print both values.

---

## 15. Setter vs Constructor

| Setter | Constructor (`__init__`) |
|---|---|
| Used to set values after creating an object. | Used to initialize values when creating an object. |
| Called manually. | Automatically called when an object is created. |
| Example: `student.set_name("saad")` | Example: `Student(NAME="saad", AGE=20)` |

---

## 16. Getter Methods

| Method | Purpose |
|---|---|
| `get_name()` | Returns the student's name. |
| `get_age()` | Returns the student's age. |
| `get_name_and_age()` | Returns both the student's name and age. |

---

## 17. Remember

- **Class:** Defines the structure of objects.
- **Object:** An instance created from a class.
- **Variables:** Store values inside objects.
- **Methods:** Perform operations.
- **Setter:** Sets or updates a value.
- **Getter:** Gets or returns a value.
- **Constructor (`__init__`):** Automatically initializes an object when it is created.
- **`self`:** Refers to the current object.
- **Multiple return values:** A method can return more than one value.
- **Unpacking:** Assigns returned values to multiple variables.

### Final Concept

In the first example, we create an object and then set its values using setter methods.

In the second example, we pass values directly during object creation using the constructor (`__init__`).

Both approaches allow us to store and access data inside objects.