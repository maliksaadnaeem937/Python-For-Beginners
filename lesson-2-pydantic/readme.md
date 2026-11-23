# Introduction to Pydantic

A beginner-friendly introduction to **Pydantic in Python**, covering type hinting, data validation, creating Pydantic models, accessing model attributes, converting models into dictionaries, and defining validation constraints.

## Learning Objectives

By the end of this lesson, students will understand:

- Three ways of declaring variables in Python.
- The difference between type hinting and data validation.
- What Pydantic is and why we use it.
- How to install Pydantic.
- How to create models using `BaseModel`.
- How Pydantic handles invalid and missing data.
- How to access model attributes.
- How to convert Pydantic models into dictionaries using `model_dump()`.
- How to use `Field()` to define validation constraints.
- How to define optional fields with default values.

## 1. Three Ways of Declaring Variables in Python

In Python, we can declare variables in three different ways.

### First: Without Type Hinting

```python
name = "saad"
```

Python does not restrict the type of value we assign to the variable.

### Second: With Type Hinting

```python
name: str = "saad"
```

Type hinting tells Python that `name` is expected to store a string.

However, type hinting does not strictly enforce the data type at runtime.

### Third: Using Pydantic

Pydantic validates data against the rules we define.

If the provided data does not follow those rules, Pydantic raises a `ValidationError`.

## 2. Installation

Install Pydantic using pip:

```bash
pip install pydantic
```

## 3. Creating Our First Pydantic Model

First, import `BaseModel` from Pydantic.

```python
from pydantic import BaseModel,Field

class Student(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
```

### Creating an Object

```python
student = Student(name="Saad", age=22)

print(student)
```

Output:

```text
name='Saad' age=22
```

### What Happens When We Provide Incorrect Data?

```python
student = Student(name="Saad", age="twenty")
```

Pydantic raises a `ValidationError` because `"twenty"` cannot be converted into an integer.

**Important:** Pydantic can automatically convert compatible values in its default mode. For example, `"22"` can be converted into `22`.

### What Happens When We Miss a Required Field?

```python
student = Student(name="Saad")
```

Pydantic raises a `ValidationError` because `age` is required but was not provided.

## 4. Accessing Model Attributes

We can access the values of a Pydantic object using dot notation.

```python
student = Student(name="Saad", age=22)

print(student.name)
print(student.age)
```

Output:

```text
Saad
22
```

## 5. Converting a Pydantic Model into a Dictionary

We can convert a Pydantic object into a Python dictionary using `model_dump()`.

```python
student = Student(name="Saad", age=22)

student_data = student.model_dump()

print(student_data)
```

Output:

```python
{'name': 'Saad', 'age': 22}
```

---

# 6. Pydantic Blueprint – Student Registration

Now let's work with a more practical example.

Before writing a Pydantic model, we will first create a blueprint. This blueprint describes the variables, their data types, whether they are required or optional, and the constraints they must follow.

Students will use this blueprint to write the Pydantic model themselves.

| Variable name | Datatype | Required / Optional | Constraint |
|---|---|---|---|
| name | String | Required | Minimum 3, maximum 50 characters |
| age | Integer | Required | Between 16 and 60 |
| email | Email | Required | String |
| cgpa | Float | Required | Between 0.0 and 4.0 |
| phone | String | Optional | Default: "Not Provided" |
| is_active | Boolean | Optional | Default: True |
| skills | List of Strings | Optional | Default: Empty list; if provided, at least 1 skill |
| city | String | Optional | Default: "Islamabad" |
| semester | Integer | Optional | Default: 1; between 1 and 8 |
| scholarship | Boolean | Optional | Default: False |

**Important Note:**

Whenever a field is optional, do not forget to provide a default value.

For example:

- `phone` → Default: `"Not Provided"`
- `city` → Default: `"Islamabad"`
- `is_active` → Default: `True`
- `scholarship` → Default: `False`
- `skills` → Default: Empty list using `default_factory=list`

Remember:
- Required fields use `Field(...)`.
- Optional fields must have a default value.
- `default_factory=list` creates a new empty list for each object.

## 7. Pydantic Model – Student Registration

Students should implement the above blueprint using Pydantic.

```python
from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=16, le=60)
    email: str = Field(...)
    cgpa: float = Field(..., ge=0.0, le=4.0)
    phone: str = Field(default="Not Provided")
    is_active: bool = Field(default=True)
    skills: list[str] = Field(default_factory=list, min_length=1)
    city: str = Field(default="Islamabad")
    semester: int = Field(default=1, ge=1, le=8)
    scholarship: bool = Field(default=False)
```

## 8. Key Concepts

| Concept | Purpose |
|---|---|
| BaseModel | Creates a Pydantic model |
| Field() | Defines field constraints and defaults |
| ... | Indicates a required field |
| default="Islamabad" | Sets a default string value |
| default=True | Sets a default Boolean value |
| default=False | Sets a default Boolean value |
| default_factory=list | Creates a new empty list for each object |
| model_dump() | Converts a model into a dictionary |
| ValidationError | Indicates invalid input data |

## 9. Important Notes

- Python type hints do not enforce types at runtime.
- Pydantic validates data when creating model instances.
- Pydantic converts compatible values in its default validation mode.
- Required fields must be provided.
- Optional fields should always have a default value.
- A default value is used when an optional field is not provided.
- `default_factory=list` creates a separate empty list for every model instance.
- `Field(...)` is used for required fields.
- `Field(default=value)` is used for optional fields with default values.

## Requirements

- Python 3.10+
- Pydantic

---

**Topic:** Python Data Validation with Pydantic  
**Level:** Beginner