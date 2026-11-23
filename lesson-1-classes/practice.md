# Python OOP – Practice Problems

Try to solve these problems yourself without looking at the solutions.

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

## Problem 4: Rectangle Class

Create a class called `Rectangle`.

- Create two variables: `length` and `width`.
- Create a setter method `set_dimensions()` to set both values.
- Create a getter method `get_dimensions()` to get both values.
- Create another method called `calculate_area()` to calculate the area of the rectangle.
- Create an object and set length to `10` and width to `5`.
- Print the area.

Formula:

```text
Area = Length × Width
```

**Expected Output:**

```text
Area: 50
```

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

## Practice Rules

1. Use classes to create all five problems.
2. Create objects from those classes.
3. Use setter methods to set values.
4. Use getter methods to access values.
5. Use `self` to access variables inside objects.
6. Try to solve without copying examples.

**Goal:** Understand how objects store values and how methods are used to set, get, and modify those values.