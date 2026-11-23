# Pydantic – Student Practice Assignment

**Topic:** Introduction to Pydantic  
**Total Questions:** 11  
**Sections:** 6 Theoretical + 5 Practical

---

# Section A: Theoretical Questions

**Q1.** What is the difference between a normal Python variable, a variable with type hinting, and a Pydantic model?

**Q2.** What is Pydantic, and why do we use it in Python applications?

**Q3.** What is the purpose of `BaseModel` in Pydantic? Explain how to create a Pydantic model using it.

**Q4.** What is the difference between required and optional fields in Pydantic? Why should we provide a default value for optional fields?

**Q5. Scenario-Based Question: Understanding Optional Fields**

Imagine you are developing a student registration system.

A student can provide their city during registration, but providing a city is not compulsory.

The system should work in two different situations:

**Situation 1: User Does Not Provide a Value**

If the student does not provide their city, the system should automatically assign `"Islamabad"` as the default city.

**Situation 2: User Provides a Value**

If the student provides their city, the system should accept it only if the city name contains at least 3 characters and a maximum of 30 characters.

Answer the following:

1. What does optional mean? Does it mean the user can provide a value or skip it?
2. What happens when the user does not provide the city?
3. What happens when the user provides a city?
4. How can we define a default value for an optional field?
5. How can we apply validation constraints to an optional field?

**Your Task:** Write a Pydantic model named `Student` that implements both situations.

**Hint:** You will need `Field()`, `default`, `min_length`, and `max_length`.

**Q6.** Explain the following Pydantic concepts with examples:

- `Field()`
- `Field(...)`
- `default_factory=list`
- `model_dump()`
- `ValidationError`

---

# Section B: Practical Questions

**Instructions:**

For each question:

1. Carefully read the given blueprint.
2. Create a Pydantic model using `BaseModel`.
3. Use `Field()` to apply the given constraints.
4. Provide appropriate default values for optional fields.
5. Create at least one object of your model.
6. Print the object and test its attributes.

## Q7. Employee Registration Model

Create a Pydantic model named `Employee` using the following blueprint.

| Variable name | Datatype | Required / Optional | Constraint |
|---|---|---|---|
| name | String | Required | Minimum 3, maximum 40 characters |
| age | Integer | Required | Between 18 and 60 |
| salary | Float | Required | Greater than 0 |
| department | String | Optional | Default: "IT" |
| is_remote | Boolean | Optional | Default: False |

## Q8. Product Registration Model

Create a Pydantic model named `Product` using the following blueprint.

| Variable name | Datatype | Required / Optional | Constraint |
|---|---|---|---|
| product_name | String | Required | Minimum 3, maximum 50 characters |
| price | Float | Required | Greater than 0 |
| quantity | Integer | Required | Between 1 and 1000 |
| category | String | Optional | Default: "General" |
| in_stock | Boolean | Optional | Default: True |
| tags | List of Strings | Optional | Default: Empty list |

## Q9. Course Registration Model

Create a Pydantic model named `Course` using the following blueprint.

| Variable name | Datatype | Required / Optional | Constraint |
|---|---|---|---|
| title | String | Required | Minimum 5, maximum 60 characters |
| duration | Integer | Required | Between 1 and 12 months |
| fee | Float | Required | Greater than 0 |
| instructor | String | Optional | Default: "Not Assigned" |
| is_online | Boolean | Optional | Default: True |
| topics | List of Strings | Optional | Default: Empty list |

## Q10. Bank Account Model

Create a Pydantic model named `BankAccount` using the following blueprint.

| Variable name | Datatype | Required / Optional | Constraint |
|---|---|---|---|
| account_holder | String | Required | Minimum 3, maximum 50 characters |
| account_number | String | Required | Exactly 16 digits |
| balance | Float | Required | Minimum 0 |
| account_type | String | Optional | Default: "Savings" |
| is_active | Boolean | Optional | Default: True |
| transactions | List of Floats | Optional | Default: Empty list |

## Q11. Hospital Patient Registration Model

Create a Pydantic model named `Patient` using the following blueprint.

| Variable name | Datatype | Required / Optional | Constraint |
|---|---|---|---|
| name | String | Required | Minimum 3, maximum 50 characters |
| age | Integer | Required | Between 1 and 100 |
| patient_id | String | Required | Exactly 8 characters |
| temperature | Float | Required | Between 35.0 and 42.0 |
| blood_group | String | Optional | Default: "Unknown" |
| is_admitted | Boolean | Optional | Default: False |
| symptoms | List of Strings | Optional | Default: Empty list |

---

# Submission Guidelines

For every practical question:

- Write the complete Pydantic model.
- Use the correct Python data types.
- Use `Field()` wherever constraints are required.
- Use `...` for required fields.
- Give every optional field a default value.
- Use `default_factory=list` for optional list fields.
- Create an object and print it.
- Test at least one invalid input to observe a `ValidationError`.
- Use `model_dump()` to convert the object into a dictionary.

**Important:** Do not copy an existing Pydantic model. Build each model yourself using the provided blueprint tables.

---

**End of Assignment**