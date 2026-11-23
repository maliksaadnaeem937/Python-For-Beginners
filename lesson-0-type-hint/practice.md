# Type Hinting in Python – Practice Questions

## Question 1: What is Type Hinting? (Theoretical)

Explain the following:

1. What is type hinting in Python?
2. Does type hinting enforce the data type of a variable?
3. Why do developers use type hinting?
4. What is the difference between `age: int = 20` and `age = 20`?

## Question 2: Will This Code Throw an Error? (Interview-Based)

Consider the following code:

```python
age: int = "twenty"

print(age)
```

Answer the following questions:

1. Will this code throw an error or execute successfully?
2. What will be the output?
3. Why does Python allow us to store a string inside a variable that has an `int` type hint?

## Question 3: Identify the Data Types (Practical)

Look at the following variables and identify their expected data types:

```python
name: str = "Saad"
age: int = 22
salary: float = 50000.50
is_student: bool = True
```

Answer the following:

1. What is the expected data type of `name`?
2. What is the expected data type of `age`?
3. What is the expected data type of `salary`?
4. What is the expected data type of `is_student`?

## Question 4: Write a Python Program (Practical)

Create four variables using type hinting:

- `student_name` with data type `str`.
- `student_age` with data type `int`.
- `student_fee` with data type `float`.
- `is_enrolled` with data type `bool`.

Assign appropriate values to these variables and print all four variables.

**Expected Output:**

```text
Student Name: Saad
Student Age: 22
Student Fee: 50000.0
Is Enrolled: True
```

## Question 5: Can We Change the Data Type? (Interview-Based + Practical)

Consider the following code:

```python
age: int = 22

age = "Saad"

print(age)
```

Answer the following questions:

1. Will this code execute successfully?
2. What will be the output?
3. Does the type hint `int` prevent us from assigning a string to the `age` variable?
4. If type hinting does not enforce data types, then what is its actual purpose?

