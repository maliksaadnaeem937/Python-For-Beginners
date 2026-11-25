# Python OOP – Practice Problems

Try to solve these problems yourself without looking at the solutions.

# Part 1: Practical Questions

## Problem 1: Student Class

Create a class called `Student`.

- Create a variable called `name`.
- Create a setter method `set_name()` to set the student's name.
- Create a getter method `get_name()` to get the student's name.
- Create an object of the `Student` class.
- Set the name to `"Saad"` and print the name using the getter method.

**Expected Output:**

```text
Saad
```

---

## Problem 2: Employee Class

Create a class called `Employee`.

- Create two variables: `name` and `salary`.
- Create a setter method `set_details()` to set both the name and salary.
- Create a getter method `get_details()` to return both values.
- Create an object of the `Employee` class.
- Set the employee's name to `"Ali"` and salary to `50000`.
- Print both values using the getter method.

**Expected Output:**

```text
Name: Ali
Salary: 50000
```

---

## Problem 3: Bank Account Class

Create a class called `BankAccount`.

- Create a variable called `balance`.
- Create a setter method `set_balance()` to set the initial balance.
- Create a getter method `get_balance()` to get the current balance.
- Create another method called `deposit()` that adds an amount to the current balance.
- Create an object and set the initial balance to `1000`.
- Deposit `500` into the account.
- Print the final balance using the getter method.

**Expected Output:**

```text
Final Balance: 1500
```

---

## Problem 4: Rectangle Class

Create a class called `Rectangle`.

- Create two variables: `length` and `width`.
- Create a setter method `set_dimensions()` to set both values.
- Create a getter method `get_dimensions()` to get both values.
- Create another method called `calculate_area()` to calculate the area of the rectangle.
- Create an object and set length to `10` and width to `5`.
- Print the area.

**Formula:**

```text
Area = Length × Width
```

**Expected Output:**

```text
Area: 50
```

---

## Problem 5: Car Class

Create a class called `Car`.

- Create three variables: `brand`, `model`, and `speed`.
- Create a setter method `set_details()` to set all three values.
- Create a getter method `get_details()` to get all three values.
- Create another method called `accelerate()` that increases the current speed by `20`.
- Create an object and set:
  - Brand: `"Toyota"`
  - Model: `"Corolla"`
  - Speed: `40`
- Call the `accelerate()` method.
- Print the car details and updated speed.

**Expected Output:**

```text
Brand: Toyota
Model: Corolla
Speed: 60
```

---

# Part 2: Practical Questions – Constructors

## Problem 6: Student Registration

Create a class called `Student`.

- Create two variables: `name` and `age`.
- Create a constructor `__init__()` that receives the student's name and age.
- Initialize both variables using the constructor.
- Create a getter method `get_details()` that returns both values.
- Create an object by passing `"Saad"` and `20` during object creation.
- Print the student's name and age using the getter method.

**Expected Output:**

```text
Name: Saad
Age: 20
```

---

## Problem 7: Product Class

Create a class called `Product`.

- Create three variables: `name`, `price`, and `quantity`.
- Create a constructor to initialize all three variables.
- Create a getter method `get_details()` that returns all three values.
- Create another method called `calculate_total()` that calculates the total price.

**Formula:**

```text
Total Price = Price × Quantity
```

Create an object with the following values:

- Name: `"Laptop"`
- Price: `100000`
- Quantity: `2`

Print the product details and total price.

**Expected Output:**

```text
Name: Laptop
Price: 100000
Quantity: 2
Total Price: 200000
```

---

## Problem 8: Bank Account With Constructor

Create a class called `BankAccount`.

- Create two variables: `account_holder` and `balance`.
- Create a constructor to initialize both variables.
- Create a getter method `get_balance()` to return the current balance.
- Create a method called `deposit()` that receives an amount and adds it to the current balance.
- Create another method called `withdraw()` that receives an amount and subtracts it from the current balance.
- Create an object with the account holder name `"Ali"` and initial balance `5000`.
- Deposit `2000`.
- Withdraw `1000`.
- Print the account holder's name and final balance.

**Expected Output:**

```text
Account Holder: Ali
Final Balance: 6000
```

---

## Problem 9: Mobile Phone Class

Create a class called `MobilePhone`.

- Create three variables: `brand`, `model`, and `price`.
- Create a constructor to initialize all three variables.
- Create a getter method `get_details()` that returns all three values.
- Create a setter method `set_price()` to update the mobile's price.
- Create a method called `apply_discount()` that reduces the price by `10%`.
- Create an object with the following values:
  - Brand: `"Samsung"`
  - Model: `"S24"`
  - Price: `200000`
- Apply the discount.
- Print the updated mobile details.

**Expected Output:**

```text
Brand: Samsung
Model: S24
Price: 180000.0
```

---

## Problem 10: Course Enrollment

Create a class called `Course`.

- Create three variables: `course_name`, `teacher_name`, and `students_enrolled`.
- Create a constructor to initialize all three variables.
- Create a getter method `get_details()` that returns all three values.
- Create a method called `enroll_student()` that increases the number of enrolled students by `1`.
- Create a setter method `set_teacher()` to update the teacher's name.
- Create an object with the following values:
  - Course Name: `"Python Programming"`
  - Teacher Name: `"Ahmed"`
  - Students Enrolled: `30`
- Enroll one new student.
- Change the teacher's name to `"Saad"`.
- Print the updated course details.

**Expected Output:**

```text
Course: Python Programming
Teacher: Saad
Students Enrolled: 31
```

---

# Part 3: Theoretical Questions

## Question 11: What are Objects?

Answer the following:

1. What are objects in Python?
2. Do objects occupy memory?
3. What do objects contain?
4. Why do we use objects?

---

## Question 12: What are Classes?

Answer the following:

1. What is a class in Python?
2. Why do we create classes?
3. Is a class an object or a blueprint for creating objects?
4. What happens when we create an object from a class?

---

## Question 13: What are Variables and Methods Inside Objects?

Answer the following:

1. What are variables inside objects used for?
2. What are methods inside objects?
3. What is the difference between a variable and a method?
4. Can methods access variables inside objects?

---

## Question 14: What are Getters and Setters?

Answer the following:

1. What is a setter method?
2. What is a getter method?
3. Why do we use setter methods?
4. Why do we use getter methods?
5. What is the difference between `set_name()` and `get_name()`?

---

## Question 15: What is `self` in Python?

Answer the following:

1. What is `self`?
2. Why do we use `self` inside class methods?
3. What does `self.name` mean?
4. What is the difference between `name` and `self.name`?
5. Does `self` refer to the current object?

---

# Part 4: Interview-Based Questions

## Question 16

What is the difference between a class and an object?

## Question 17

What is the difference between a method and a function?

## Question 18

Can we create multiple objects from a single class?

## Question 19

What happens when we create an object using:

```python
student = Student()
```

## Question 20

Why do we use `self` when defining methods inside a class?

---

# Part 5: Constructor-Based Questions

## Question 21: What is a Constructor?

Answer the following:

1. What is a constructor in Python?
2. What is the name of the constructor method in Python?
3. When does the constructor execute?
4. Why do we use constructors?

---

## Question 22: Understanding `__init__()`

Answer the following:

1. What is the purpose of `__init__()`?
2. Is `__init__()` called manually or automatically?
3. What happens when we create an object of a class containing `__init__()`?
4. Can we define variables inside `__init__()`?

---

## Question 23: Passing Values Through a Constructor

Consider the following code:

```python
class Student:
    def __init__(self, NAME, AGE):
        self.name = NAME
        self.age = AGE


student = Student("Saad", 20)
```

Answer the following:

1. What values are passed to the constructor?
2. What does `NAME` receive?
3. What does `AGE` receive?
4. What is stored inside `student.name`?
5. What is stored inside `student.age`?

---

## Question 24: Constructor vs Setter

Answer the following:

1. What is the difference between a constructor and a setter method?
2. When does a constructor execute?
3. When do we call a setter method?
4. Can we update an object's value after creating it using a setter?
5. Why might we use a constructor instead of a setter when creating an object?

---

## Question 25: Creating Objects With Constructors

Consider the following code:

```python
class Employee:
    def __init__(self, NAME, SALARY):
        self.name = NAME
        self.salary = SALARY


employee = Employee("Ali", 50000)
```

Answer the following:

1. What happens when `Employee("Ali", 50000)` executes?
2. How many objects are created in this code?
3. Why do we pass `"Ali"` and `50000` during object creation?
4. What is the purpose of `self.name = NAME`?
5. What is the purpose of `self.salary = SALARY`?
6. What would happen if we created the object without passing the required values?

---

# Practice Rules

1. Use classes to solve all practical problems.
2. Create objects from those classes.
3. Use setter methods wherever required.
4. Use getter methods wherever required.
5. Use constructors wherever required.
6. Use `self` to access variables inside objects.
7. Try to solve without copying examples.
8. Try to answer theoretical questions in your own words.
9. Understand the logic instead of memorizing the code.

# Goal

Understand how objects store values and how methods are used to set, get, and modify those values.

Also understand how classes define the structure of objects, how constructors initialize objects, how we pass values during object creation, and how objects can perform operations using their own data.