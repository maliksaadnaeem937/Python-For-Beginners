# Python OOP – Practice Problems

Try to solve these problems yourself without looking at the solutions.

## Part 1: Practical Questions

### Problem 1: Student Class

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

### Problem 2: Employee Class

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

### Problem 3: Bank Account Class

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

### Problem 4: Rectangle Class

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

### Problem 5: Car Class

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

## Part 2: Theoretical Questions

### Question 1: What are Objects?

Answer the following:

1. What are objects in Python?
2. Do objects occupy memory?
3. What do objects contain?
4. Why do we use objects?

### Question 2: What are Classes?

Answer the following:

1. What is a class in Python?
2. Why do we create classes?
3. Is a class an object or a blueprint for creating objects?
4. What happens when we create an object from a class?

### Question 3: What are Variables and Methods Inside Objects?

Answer the following:

1. What are variables inside objects used for?
2. What are methods inside objects?
3. What is the difference between a variable and a method?
4. Can methods access variables inside objects?

### Question 4: What are Getters and Setters?

Answer the following:

1. What is a setter method?
2. What is a getter method?
3. Why do we use setter methods?
4. Why do we use getter methods?
5. What is the difference between `set_name()` and `get_name()`?

### Question 5: What is `self` in Python?

Answer the following:

1. What is `self`?
2. Why do we use `self` inside class methods?
3. What does `self.name` mean?
4. What is the difference between `name` and `self.name`?
5. Does `self` refer to the current object?

---

## Part 3: Interview-Based Questions

### Question 1

What is the difference between a class and an object?

### Question 2

What is the difference between a method and a function?

### Question 3

Can we create multiple objects from a single class?

### Question 4

What happens when we create an object using:

```python
student = Student()
```

### Question 5

Why do we use `self` when defining methods inside a class?

---

## Practice Rules

1. Use classes to create all five problems.
2. Create objects from those classes.
3. Use setter methods to set values.
4. Use getter methods to access values.
5. Use `self` to access variables inside objects.
6. Try to solve without copying examples.
7. Try to answer theoretical questions in your own words.

## Goal

Understand how objects store values and how methods are used to set, get, and modify those values. Also understand how classes define the structure of objects and how we create objects from classes.