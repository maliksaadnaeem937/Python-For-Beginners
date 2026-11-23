# Understanding Classes and Objects in Python

## 1. What are Objects?

The real things are objects.

Objects occupy memory, and objects are useful.

Objects have variables and methods in them.

Inside objects, we have variables and methods.

Variables inside objects are used to store values, and methods inside objects are used to perform operations.

## 2. How Do We Access Variables Inside Objects?

We can access the variables inside objects using methods.

Suppose we have an object with a variable called `name`.

Now we want to give a value to this variable `name`, which is inside the object.

We will use a method to give or set the value to the variable `name`.

This method will be called a **Setter**.

Setters are the methods used to give values to variables inside an object.

## 3. What are Getters?

Now let's suppose the `name` variable has some value (`"saad"`) which we gave using the setter method.

Now we want to access or get the value of the `name` variable.

For this, we can use another method called `get_name()` to get the value of the variable.

This method is called a **Getter**.

Getters are the methods used to get or access the values of variables inside an object.

## 4. What Do Objects Contain?

So, inside objects, we have variables that store values and methods.

Methods are used either to set the values of variables that are inside the object or to get the values of variables inside the object.

- Variables store values inside objects.
- Setter methods are used to give values to variables inside objects.
- Getter methods are used to get values from variables inside objects.

## 5. How Do We Create Objects?

Now the question is, how do we create objects?

To create objects, we define classes.

When we write a class, inside it we define the structure of how our object will look.

For example, in this case, we can create a class called `Student` with:

- A variable called `name`.
- Two methods called `get_name()` and `set_name()`.

These two methods will be used to set and get the value of the variable `name`.

Then we can create an object from this class.

The object will now have the variables and methods that we defined in the class.

We don't access the variables of the class directly. First, we create objects of the class, then give values to the variables inside the objects, and then access those values.

---

## 6. Code Example

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

## 7. Understanding the Flow

1. We create a class called `Student`.
2. Inside the class, we define a variable called `name`.
3. We define a setter method called `set_name()` to give a value to the `name` variable.
4. We define a getter method called `get_name()` to get the value of the `name` variable.
5. We create an object called `student` from the `Student` class.
6. We call `student.set_name("saad")` to set the value of the name variable.
7. We call `student.get_name()` to get the value of the name variable.
8. Finally, we print the value.

**Remember:** Classes define the structure of objects. Objects contain variables and methods. Setter methods set values, and getter methods get values.