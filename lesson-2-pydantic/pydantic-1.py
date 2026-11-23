
from pydantic import BaseModel,Field

class Student(BaseModel):
    name: str=Field(...)
    age: int=Field(...)

student = Student(name="Saad", age=22)

print(student)
