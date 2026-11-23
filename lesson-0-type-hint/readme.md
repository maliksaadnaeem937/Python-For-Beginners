# Type Hinting in Python

## What is Type Hinting?

Type hinting is a method used in Python to tell which data type a variable should have.

It does not enforce that data type. Meaning, it is just used for developers to keep track of what kind of data a variable will contain.

And if we want to store any other data type in that variable, we can store it.

## Example

```python
age: int = "ten"

print(age)
```

**Output:**

```text
ten
```

## Why does it not throw an error?

It will not throw any error because `int` is only used for developers, not to enforce the `int` data type on variable `age`.

Python does not automatically stop us from assigning a different data type to a variable just because we used type hinting.

## Another Example

```python
name: str = "Saad"
age: int = 22
salary: float = 50000.50
is_student: bool = True

print(name)
print(age)
print(salary)
print(is_student)
```

**Output:**

```text
Saad
22
50000.5
True
```

## Important Things to Remember

- `int` means integer.
- `str` means string.
- `float` means decimal number.
- `bool` means True or False.
- Type hinting helps developers understand what kind of data a variable is expected to contain.
- Type hinting does not enforce data types at runtime.

**In simple words:** Type hinting tells developers what type of data a variable is expected to contain, but Python does not force that variable to contain only that type.